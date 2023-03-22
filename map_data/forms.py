from django import forms
from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Field,Fieldset
from .models import Taichung110

map_area = {
    '中區':'Central District',
    '東區':'East District',
    '南區':'South District',
    '西區':'West District',
    '北區':'North District',
    '西屯區':'Xitun District',
    '南屯區':'Nantun District',
    '北屯區':'Beitun District',
    '豐原區':'Fengyuan District',
    '東勢區':'Dongshi District',
    '大甲區':'Dajia District',
    '清水區':'Qingshui District',
    '沙鹿區':'Shalu District',
    '梧棲區':'Wuqi District',
    '后里區':'Houli District',
    '神岡區':'Shengang District',
    '潭子區':'Tanzi District',
    '大雅區':'Daya District',
    '新社區':'Xinshe District',
    '石岡區':'Shigang District',
    '外埔區':'Waipu District',
    '大安區':'Da’an District',
    '烏日區':'Wuri District',
    '大肚區':'Dadu District',
    '龍井區':'Longjing District',
    '霧峰區':'Wufeng District',
    '太平區':'Taiping District',
    '大里區':'Dali District',
    '和平區':'Heping District'
}

class Form(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields['min_price'].label = False
        self.fields['max_price'].label = False
        self.fields['min_age'].label = False
        self.fields['max_age'].label = False
        self.fields['min_floor_no'].label = False
        self.fields['max_floor_no'].label = False
        self.fields['min_total_floor'].label = False
        self.fields['max_total_floor'].label = False
        self.fields['area'].label = False
        self.helper.layout = Layout(
            Field("b_type", css_class="form-select", css_id="b_type"),
            Field("min_price", placeholder="Min Price", id="min_price", css_class="text-right"),
        )
    CHOICES = (
        (0, "Select Type"),
        (1, "Townhouse"),# 透天
        (2, "Studio"), # 套房
        (3, "Mid-rise"), # 公寓
        (4, "High-rise"), # 華廈
        (5, "Mansion") # 大樓
    )

    area = list(Taichung110.objects.values('鄉鎮市區').distinct())
    area_choice = [(0,"Select Area")]
    count = 0
    for item in area:
        area_choice.append((item['鄉鎮市區'],map_area[item['鄉鎮市區']]))

    area = forms.ChoiceField(choices = tuple(area_choice),label="Area",  initial='Choosing the area', widget=forms.Select(), required=False)
    b_type = forms.ChoiceField(choices = CHOICES,label="Type",  initial='Choosing a type of house', widget=forms.Select(attrs = {'onchange' : "typeSelected(this.value)"}), required=False)
    min_price = forms.IntegerField(min_value=0, initial='MIN', required=False, widget=forms.NumberInput(attrs={'style': "text-align: right;"}), error_messages={'min_value': 'The value must be greater than or equal to 0'})
    max_price = forms.IntegerField(min_value=500, initial='MAX', required=False, widget=forms.NumberInput(attrs={'style': "text-align: right;"}), error_messages={'min_value': 'The value must be greater than or equal to 500萬'})
    min_age = forms.IntegerField(min_value=1, max_value=60, initial='MIN', required=False, widget=forms.NumberInput(attrs={'style': "text-align: right;"}), error_messages={'min_value': 'The value must be greater than or equal to 1', 'max_value': 'The value must be less than or equal to 60'})
    max_age = forms.IntegerField(min_value=1, max_value=60, initial='MAX', required=False, widget=forms.NumberInput(attrs={'style': "text-align: right;"}), error_messages={'min_value': 'The value must be greater than or equal to 1', 'max_value': 'The value must be less than or equal to 60'})
    min_floor_no = forms.IntegerField(min_value=1, max_value=50, initial='MIN', required=False, widget=forms.NumberInput(attrs={'style': "text-align: right;"}), error_messages={'min_value': 'The value must be greater than or equal to 1', 'max_value': 'The value must be less than or equal to 50'})
    max_floor_no = forms.IntegerField(min_value=1, max_value=50, initial='MAX', required=False, widget=forms.NumberInput(attrs={'style': "text-align: right;"}), error_messages={'min_value': 'The value must be greater than or equal to 1', 'max_value': 'The value must be less than or equal to 50'})
    min_total_floor = forms.IntegerField(min_value=1, max_value=15, initial='MIN', required=False, widget=forms.NumberInput(attrs={'style': "text-align: right;"}), error_messages={'min_value': 'The value must be greater than or equal to 1', 'max_value': 'The value must be less than or equal to 15'})
    max_total_floor = forms.IntegerField(min_value=1, max_value=15, initial='MAX', required=False, widget=forms.NumberInput(attrs={'style': "text-align: right;"}), error_messages={'min_value': 'The value must be greater than or equal to 1', 'max_value': 'The value must be less than or equal to 15'})
