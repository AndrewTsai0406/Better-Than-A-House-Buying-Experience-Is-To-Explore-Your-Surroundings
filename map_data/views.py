from django.shortcuts import render
from django.db import connection
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from enum import Enum
from .forms import Form

select_column = "ST_Y(ST_Transform(geom,4326)), ST_X(ST_Transform(geom,4326)), 土地位置建物門牌, id, 總價元, 建物型態, trans_floor, total_floor, age_year,ping, near_police, near_university, near_senior_high_school, near_junior_high_school, near_elementary_school, near_activities, near_hospital, near_park, near_religious_activities, near_scenic_spot, near_mrt"
class subType(Enum):
	police = 'o'
	park = 'p'
	religious = 'r'
	university = 'u'
	senior = 's'
	junior = 'j'
	elementary = 'e'
	activities = 'a'
	hospital = 'h'
	scenic = 'c'
	mrt = 'm'

class graphTag(Enum):
	Police = 'o'
	Park = 'p'
	Religious = 'r'
	University = 'u'
	Senior_school = 's'
	Junior_school = 'j'
	Elementary_school = 'e'
	Active = 'a'
	Hospital = 'h'
	Scenic_spot = 'c'
	MRT = 'm'

form_column = {'b_type' : '建物型態',
	'area':'鄉鎮市區',
	'min_price' : '總價元',
	'max_price' : '總價元',
	'min_age' : 'age_year',
	'max_age' : 'age_year',
	'min_floor_no' : 'trans_floor',
	'max_floor_no' : 'trans_floor',
	'min_total_floor' : 'total_floor',
	'max_total_floor' : 'total_floor'}

class mapArea(Enum):
	中區='Central District'
	東區='East District'
	南區='South District'
	西區='West District'
	北區='North District'
	西屯區='Xitun District'
	南屯區='Nantun District'
	北屯區='Beitun District'
	豐原區='Fengyuan District'
	東勢區='Dongshi District'
	大甲區='Dajia District'
	清水區='Qingshui District'
	沙鹿區='Shalu District'
	梧棲區='Wuqi District'
	后里區='Houli District'
	神岡區='Shengang District'
	潭子區='Tanzi District'
	大雅區='Daya District'
	新社區='Xinshe District'
	石岡區='Shigang District'
	外埔區='Waipu District'
	大安區='Da’an District'
	烏日區='Wuri District'
	大肚區='Dadu District'
	龍井區='Longjing District'
	霧峰區='Wufeng District'
	太平區='Taiping District'
	大里區='Dali District'
	和平區='Heping District'

def index(request):
	page = request.GET.get('page')

	default_conditions = " (建物型態 in ('套房', '公寓', '華廈', '大樓') AND trans_floor > 0) OR (建物型態='透天厝' AND total_floor > 0)"
	limit = " LIMIT 30"
	set_limit = False
	post = 0
	if 'form' in request.session: 
		store_form_data = request.session['form']
		print(store_form_data)
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			conditions, store_form_data = generate_SQL_conditions_post(form)
			if conditions == '':
				set_limit = True
			conditions = deal_default_SQL(conditions, default_conditions)

		request.session['form'] = store_form_data
		post = 1
	else:
		post = request.GET.get('p')
		if not post or post == 0 or post=='None' or not store_form_data:
			form = Form()
			conditions = " WHERE "+default_conditions
			set_limit = True
		else:
			form = Form(store_form_data)
			conditions = generate_SQL_conditions_session(store_form_data)
			conditions = deal_default_SQL(conditions, default_conditions)
			
	print(conditions)
	cursor = connection.cursor()
	if set_limit:
		query_sql = "SELECT "+select_column+" FROM taichung110"+conditions+" ORDER BY RANDOM() "+limit+";"
	else:
		query_sql = "SELECT "+select_column+" FROM taichung110"+conditions+" ORDER BY RANDOM();"
	
	query_sql = "SELECT "+select_column+" FROM taichung110"+conditions+" ORDER BY RANDOM() "+limit+";"
	cursor.execute(query_sql)
	columns = [col[0] for col in cursor.description]
	result = cursor.fetchall()
	connection.close()

	pa = request.GET.get('pa')
	if pa:
		result = filter_result(pa, result, columns)

	# Control paging data
	limit = 5
	paginator = Paginator(result, limit)
	try:
		result = paginator.page(page)
	except PageNotAnInteger:
		result = paginator.page(1)
	except EmptyPage:
		result = paginator.page(paginator.num_pages)

	decrete, radial = generate_output(result, columns)
	g_args = generate_args_graph_db(radial,pa)

	return render(request, 'index.html', {"radial": radial, "decrete": decrete, 'form': form, "raw_data": result, "post": post, "pa":pa, "g_args":g_args})


currency_format = "${:,.2f}"
def generate_output(result, columns):
	decrete = []
	radial = []
	count = 0
	for row in result:
		child = []
		id = row[3]
		house_data = {"type": "house",
        "id": id,
        "name": row[2],
		"lat": row[0],
		"lng": row[1],
		"price": currency_format.format(row[4]),
		"b_type": map_building_type(False, True, row[5]),
		"trans_floor": row[6],
		"total_floor": row[7],
		"age": row[8],
		"ping": row[9]}
		decrete.append(house_data)
		for i in range(len(columns)):
			if columns[i].startswith('near'):
				sub_data = {
					"type": "facility",
					"subtype": columns[i].split('_')[1],
					"id": str(id)+"_"+subType[columns[i].split('_')[1]].value,
					"name": row[i]
            	}
				decrete.append(sub_data)
				child.append(sub_data)
		house_data["address"] = row[2]
		house_data["child"] = child
		radial.append(house_data)
		
		count+=1
	return decrete, radial

switch_d = { '0': None, '1': "透天厝", '2': "套房", '3': "公寓", '4': "華廈", '5': "大樓" }
switch_e = {"透天厝" : "Townhouse",  "套房" : "Studio", "公寓" : "Mid-rise", "華廈" : "High-rise", "大樓" : "Mansion"}

def map_building_type(fromDigit, fromChinese, data):
	if fromDigit:
		return switch_d[data]
	if fromChinese:
		return switch_e[data]

def generate_args_graph_db(radial, pa):
	if radial:
		args = "MATCH(house:House)-[p]->(pos) WHERE house.houseID in "
		houses = "["
		pa_args = ""
		for house in radial:
			if len(houses) > 1:
				houses+=","
			houses+="'"+str(house['id'])+"'"
		houses+="]"
		if pa and len(pa) > 0:
			pa_args += " and p.pos in ["
			for a in pa:
				if not pa_args.endswith("["):
					pa_args+=","
				pa_args+="'"+graphTag(a).name+"'"
			
			pa_args += "]"
		return args+houses+pa_args+" return house,pos;"
	else:
		return ""

def generate_SQL_conditions_post(form):
	conditions = ''
	store_form_data = {}
	for c in form_column.items():
		if c[0] == 'area':
			value = form.cleaned_data[c[0]]
			if not value == None and not value == 0 and not value == "0":
				if not conditions == '':
					conditions+=' AND '
				conditions += (c[1]+' = \''+value+'\' ')
				store_form_data[c[0]]=mapArea[value].name
		if c[0] == 'b_type':
			value = map_building_type(True, False, form.cleaned_data[c[0]])
			if not value == None:
				conditions += (c[1]+'=\''+value+'\' ')
				store_form_data[c[0]]=form.cleaned_data[c[0]]
		elif c[0].startswith('min'):
			value = form.data[c[0]]
			if not value == '':
				if not conditions == '':
					conditions+=' AND '
				if c[0].endswith('price'):
					value += '000'
				conditions += (c[1]+' >= '+value+' ')
				store_form_data[c[0]]=form.data[c[0]]
		if c[0].startswith('max'):
			value = form.data[c[0]]
			if not value == '':
				if not conditions == '':
					conditions+=' AND '
				if c[0].endswith('price'):
					value += '000'
				conditions += (c[1]+' <= '+value+' ')
				store_form_data[c[0]]=form.data[c[0]]

	return conditions, store_form_data

def generate_SQL_conditions_session(store_form_data):
	conditions = ''
	for c in form_column.items():
		if not c[0] in store_form_data:
			continue
		if c[0] == 'b_type':
			value = map_building_type(True, False, store_form_data[c[0]])
			conditions += (c[1]+'=\''+value+'\' ')
		elif c[0] == 'area':
			value = store_form_data[c[0]]
			if not conditions == '':
				conditions+=' AND '
			conditions += (c[1]+'=\''+value+'\' ')
		elif c[0].startswith('min'):
			value = store_form_data[c[0]]
			if not conditions == '':
				conditions+=' AND '
			if c[0].endswith('price'):
				value += '000'
			conditions += (c[1]+' >= '+value+' ')
		if c[0].startswith('max'):
			value = store_form_data[c[0]]

			if not conditions == '':
				conditions+=' AND '
			if c[0].endswith('price'):
				value += '000'
			conditions += (c[1]+' <= '+value+' ')

	return conditions

def deal_default_SQL(conditions, default_conditions):
	if not conditions == '':
		if not 'trans_floor >=' in conditions and '建物型態' in conditions and not '建物型態=\'透天厝\'' in conditions:
			conditions = " WHERE "+conditions+' AND trans_floor > 0'
		elif not 'trans_floor >=' in conditions and not '建物型態' in conditions:
			conditions = " WHERE "+conditions+' AND ('+default_conditions+')'
		elif 'trans_floor >=' in conditions and not '建物型態' in conditions:
			conditions = " WHERE "+conditions+' AND 建物型態 in (\'套房\', \'公寓\', \'華廈\', \'大樓\')'
		else:
			conditions = " WHERE "+conditions
	else:
		conditions = " WHERE "+default_conditions
	return conditions


def add_form_value(form, store_form_data):
	for item in store_form_data.items():
		form[item[0]] = item[1]

def filter_result(pa, result,columns):
	filtered_result = []
	for row in result:
		check = True
		dict_row = dict(zip(columns,row))
		for i in range(len(columns)):
			for p in pa:
				if subType(p).name in columns[i]:
					if not dict_row[columns[i]]:
						check = False

		if check:
			filtered_result.append(row)

	return filtered_result