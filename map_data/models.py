# coding:utf-8
from django.db import models


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
        db_table = 'taichung110'