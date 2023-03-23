# coding:utf-8
from django.db import models

class ActivityCF(models.Model):
    gid = models.AutoField(primary_key=True)
    id = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    location = models.CharField(max_length=254, blank=True, null=True)
    add = models.CharField(max_length=254, blank=True, null=True)
    region = models.CharField(max_length=254, blank=True, null=True)
    town = models.CharField(max_length=254, blank=True, null=True)
    tel = models.CharField(max_length=254, blank=True, null=True)
    org = models.CharField(max_length=254, blank=True, null=True)
    start = models.CharField(max_length=254, blank=True, null=True)
    end = models.CharField(max_length=254, blank=True, null=True)
    cycle = models.CharField(max_length=254, blank=True, null=True)
    noncycle = models.CharField(max_length=254, blank=True, null=True)
    website = models.CharField(max_length=254, blank=True, null=True)
    picture1 = models.CharField(max_length=254, blank=True, null=True)
    picdes_be1 = models.CharField(max_length=254, blank=True, null=True)
    picture2 = models.CharField(max_length=254, blank=True, null=True)
    picdes_be2 = models.CharField(max_length=254, blank=True, null=True)
    picture3 = models.CharField(max_length=254, blank=True, null=True)
    picdes_be3 = models.CharField(max_length=254, blank=True, null=True)
    px = models.CharField(max_length=254, blank=True, null=True)
    py = models.CharField(max_length=254, blank=True, null=True)
    class1 = models.CharField(max_length=254, blank=True, null=True)
    class2 = models.CharField(max_length=254, blank=True, null=True)
    map = models.CharField(max_length=254, blank=True, null=True)
    travel_nfo = models.CharField(max_length=254, blank=True, null=True)
    parkin_nfo = models.CharField(max_length=254, blank=True, null=True)
    remarks = models.CharField(max_length=254, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'activity_c_f'


class BikeRoadF(models.Model):
    gid = models.AutoField(primary_key=True)
    id = models.CharField(max_length=254, blank=True, null=True)
    iotid = models.CharField(max_length=254, blank=True, null=True)
    roadid = models.CharField(max_length=254, blank=True, null=True)
    roadno = models.CharField(max_length=254, blank=True, null=True)
    systype = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    s_placedes = models.CharField(max_length=254, blank=True, null=True)
    e_placedes = models.CharField(max_length=254, blank=True, null=True)
    toldes_ibe = models.CharField(max_length=254, blank=True, null=True)
    descri_ion = models.CharField(max_length=254, blank=True, null=True)
    bike_l_gth = models.CharField(max_length=254, blank=True, null=True)
    bike_width = models.CharField(max_length=254, blank=True, null=True)
    road_width = models.CharField(max_length=254, blank=True, null=True)
    hight = models.CharField(max_length=254, blank=True, null=True)
    slope = models.CharField(max_length=254, blank=True, null=True)
    lamp = models.CharField(max_length=254, blank=True, null=True)
    direction = models.CharField(max_length=254, blank=True, null=True)
    roadtype = models.CharField(max_length=254, blank=True, null=True)
    pave = models.CharField(max_length=254, blank=True, null=True)
    class1 = models.CharField(max_length=254, blank=True, null=True)
    class2 = models.CharField(max_length=254, blank=True, null=True)
    class3 = models.CharField(max_length=254, blank=True, null=True)
    structure = models.CharField(max_length=254, blank=True, null=True)
    cs = models.CharField(max_length=254, blank=True, null=True)
    add = models.CharField(max_length=254, blank=True, null=True)
    tel = models.CharField(max_length=254, blank=True, null=True)
    region = models.CharField(max_length=254, blank=True, null=True)
    town = models.CharField(max_length=254, blank=True, null=True)
    travel_nfo = models.CharField(max_length=254, blank=True, null=True)
    picture1 = models.CharField(max_length=254, blank=True, null=True)
    picdes_be1 = models.CharField(max_length=254, blank=True, null=True)
    picture2 = models.CharField(max_length=254, blank=True, null=True)
    picdes_be2 = models.CharField(max_length=254, blank=True, null=True)
    picture3 = models.CharField(max_length=254, blank=True, null=True)
    picdes_be3 = models.CharField(max_length=254, blank=True, null=True)
    map = models.CharField(max_length=254, blank=True, null=True)
    gov = models.CharField(max_length=254, blank=True, null=True)
    website = models.CharField(max_length=254, blank=True, null=True)
    remarks = models.CharField(max_length=254, blank=True, null=True)
    keyword = models.CharField(max_length=254, blank=True, null=True)
    route_xy = models.CharField(max_length=254, blank=True, null=True)
    name_nb = models.CharField(max_length=254, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'bike_road_f'


class ElementarySchool(models.Model):
    學校級別 = models.CharField(max_length=20, blank=True, null=True)
    代碼 = models.CharField(max_length=10, blank=True, null=True)
    學校名稱 = models.CharField(max_length=20, blank=True, null=True)
    縣市別 = models.CharField(max_length=10, blank=True, null=True)
    鄉鎮市區 = models.CharField(max_length=10, blank=True, null=True)
    地址 = models.CharField(max_length=50, blank=True, null=True)
    電話 = models.CharField(max_length=50, blank=True, null=True)
    網址 = models.CharField(max_length=100, blank=True, null=True)
    體系別 = models.CharField(max_length=10, blank=True, null=True)
    x_坐標 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    y_坐標 = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'elementary_school'


class Hospital(models.Model):
    place_name = models.CharField(max_length=20, blank=True, null=True)
    cordinates = models.CharField(max_length=150, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'hospital'


class JuniorHighSchool(models.Model):
    學校級別 = models.CharField(max_length=20, blank=True, null=True)
    代碼 = models.CharField(max_length=10, blank=True, null=True)
    學校名稱 = models.CharField(max_length=20, blank=True, null=True)
    縣市別 = models.CharField(max_length=10, blank=True, null=True)
    鄉鎮市區 = models.CharField(max_length=10, blank=True, null=True)
    地址 = models.CharField(max_length=50, blank=True, null=True)
    電話 = models.CharField(max_length=50, blank=True, null=True)
    網址 = models.CharField(max_length=100, blank=True, null=True)
    體系別 = models.CharField(max_length=10, blank=True, null=True)
    x_坐標 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    y_坐標 = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'junior_high_school'


class Park(models.Model):
    place_name = models.CharField(max_length=20, blank=True, null=True)
    cordinates = models.CharField(max_length=150, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'park'


class Police(models.Model):
    中文單位名稱 = models.CharField(max_length=50, blank=True, null=True)
    英文單位名稱 = models.CharField(max_length=150, blank=True, null=True)
    郵遞區號 = models.CharField(max_length=150, blank=True, null=True)
    地址 = models.CharField(max_length=50, blank=True, null=True)
    電話 = models.CharField(max_length=50, blank=True, null=True)
    point_x = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    point_y = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'police'


class ReligiousActivities(models.Model):
    中文名稱 = models.CharField(max_length=50, blank=True, null=True)
    wgs84x = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    wgs84y = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    縣市 = models.CharField(max_length=10, blank=True, null=True)
    鄉鎮市區 = models.CharField(max_length=20, blank=True, null=True)
    地址 = models.CharField(max_length=50, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'religious_activities'


class RestaurantCF(models.Model):
    gid = models.AutoField(primary_key=True)
    id = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    add = models.CharField(max_length=254, blank=True, null=True)
    zipcode = models.CharField(max_length=254, blank=True, null=True)
    region = models.CharField(max_length=254, blank=True, null=True)
    town = models.CharField(max_length=254, blank=True, null=True)
    tel = models.CharField(max_length=254, blank=True, null=True)
    website = models.CharField(max_length=254, blank=True, null=True)
    picture1 = models.CharField(max_length=254, blank=True, null=True)
    picdes_be1 = models.CharField(max_length=254, blank=True, null=True)
    picture2 = models.CharField(max_length=254, blank=True, null=True)
    picdes_be2 = models.CharField(max_length=254, blank=True, null=True)
    picture3 = models.CharField(max_length=254, blank=True, null=True)
    picdes_be3 = models.CharField(max_length=254, blank=True, null=True)
    px = models.CharField(max_length=254, blank=True, null=True)
    py = models.CharField(max_length=254, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=254, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    map = models.CharField(max_length=254, blank=True, null=True)
    parkin_nfo = models.CharField(max_length=254, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'restaurant_c_f'


class ScenicSpotCF(models.Model):
    gid = models.AutoField(primary_key=True)
    id = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    zone = models.CharField(max_length=254, blank=True, null=True)
    tel = models.CharField(max_length=254, blank=True, null=True)
    add = models.CharField(max_length=254, blank=True, null=True)
    zipcode = models.CharField(max_length=254, blank=True, null=True)
    region = models.CharField(max_length=254, blank=True, null=True)
    town = models.CharField(max_length=254, blank=True, null=True)
    picture1 = models.CharField(max_length=254, blank=True, null=True)
    picdes_be1 = models.CharField(max_length=254, blank=True, null=True)
    picture2 = models.CharField(max_length=254, blank=True, null=True)
    picdes_be2 = models.CharField(max_length=254, blank=True, null=True)
    picture3 = models.CharField(max_length=254, blank=True, null=True)
    picdes_be3 = models.CharField(max_length=254, blank=True, null=True)
    map = models.CharField(max_length=254, blank=True, null=True)
    gov = models.CharField(max_length=254, blank=True, null=True)
    px = models.CharField(max_length=254, blank=True, null=True)
    py = models.CharField(max_length=254, blank=True, null=True)
    orgclass = models.CharField(max_length=254, blank=True, null=True)
    class1 = models.CharField(max_length=254, blank=True, null=True)
    class2 = models.CharField(max_length=254, blank=True, null=True)
    class3 = models.CharField(max_length=254, blank=True, null=True)
    level = models.CharField(max_length=254, blank=True, null=True)
    website = models.CharField(max_length=254, blank=True, null=True)
    parkin_nfo = models.CharField(max_length=254, blank=True, null=True)
    parkin_px = models.CharField(db_column='parkin__px', max_length=254, blank=True, null=True)
    parkin_py = models.CharField(db_column='parkin__py', max_length=254, blank=True, null=True)
    ticketinfo = models.CharField(max_length=254, blank=True, null=True)
    keyword = models.CharField(max_length=254, blank=True, null=True)
    changetime = models.CharField(max_length=254, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'scenic_spot_c_f'


class SeniorHighSchool(models.Model):
    學校級別 = models.CharField(max_length=20, blank=True, null=True)
    代碼 = models.CharField(max_length=10, blank=True, null=True)
    學校名稱 = models.CharField(max_length=20, blank=True, null=True)
    縣市別 = models.CharField(max_length=10, blank=True, null=True)
    鄉鎮市區 = models.CharField(max_length=10, blank=True, null=True)
    地址 = models.CharField(max_length=50, blank=True, null=True)
    電話 = models.CharField(max_length=50, blank=True, null=True)
    網址 = models.CharField(max_length=100, blank=True, null=True)
    體系別 = models.CharField(max_length=10, blank=True, null=True)
    x_坐標 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    y_坐標 = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'senior_high_school'


class Taichung110(models.Model):
    縣市 = models.CharField(max_length=50, blank=True, null=True)
    鄉鎮市區 = models.CharField(max_length=50, blank=True, null=True)
    交易標的 = models.CharField(max_length=50, blank=True, null=True)
    土地位置建物門牌 = models.CharField(max_length=200, blank=True, null=True)
    土地移轉總面積平方公尺 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    都市土地使用分區 = models.CharField(max_length=50, blank=True, null=True)
    非都市土地使用分區 = models.CharField(max_length=50, blank=True, null=True)
    非都市土地使用編定 = models.CharField(max_length=50, blank=True, null=True)
    交易年月日 = models.DateField(blank=True, null=True)
    交易筆棟數 = models.CharField(max_length=50, blank=True, null=True)
    移轉層次 = models.CharField(max_length=150, blank=True, null=True)
    總樓層數 = models.CharField(max_length=50, blank=True, null=True)
    建物型態 = models.CharField(max_length=50, blank=True, null=True)
    主要用途 = models.CharField(max_length=50, blank=True, null=True)
    主要建材 = models.CharField(max_length=50, blank=True, null=True)
    建築完成年月 = models.DateField(blank=True, null=True)
    建物移轉總面積平方公尺 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    建物現況格局_房 = models.SmallIntegerField(blank=True, null=True)
    建物現況格局_廳 = models.SmallIntegerField(blank=True, null=True)
    建物現況格局_衛 = models.SmallIntegerField(blank=True, null=True)
    建物現況格局_隔間 = models.CharField(max_length=1, blank=True, null=True)
    有無管理組織 = models.CharField(max_length=1, blank=True, null=True)
    總價元 = models.BigIntegerField(blank=True, null=True)
    單價元平方公尺 = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    車位類別 = models.CharField(max_length=10, blank=True, null=True)
    車位移轉總面積_平方公尺 = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    車位總價元 = models.IntegerField(blank=True, null=True)
    備註 = models.CharField(max_length=300, blank=True, null=True)
    編號 = models.CharField(max_length=20, blank=True, null=True)
    主建物面積 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    附屬建物面積 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    陽台面積 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    電梯 = models.CharField(max_length=1, blank=True, null=True)
    lat = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    long = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'taichung_110'


class Universities(models.Model):
    x_坐標 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    y_坐標 = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'universities'
