# from django.db import models
from django.contrib.gis.db import models


class SpatialRefSys(models.Model):
	srid = models.IntegerField(primary_key=True)
	auth_name = models.CharField(max_length=256, blank=True, null=True)
	auth_srid = models.IntegerField(blank=True, null=True)
	srtext = models.CharField(max_length=2048, blank=True, null=True)
	proj4text = models.CharField(max_length=2048, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'spatial_ref_sys'


class Station4326(models.Model):
	gid = models.AutoField(primary_key=True)
	field_gid = models.FloatField(db_column='__gid', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
	markid = models.CharField(max_length=11, blank=True, null=True)
	marktype1 = models.CharField(max_length=8, blank=True, null=True)
	marktype2 = models.CharField(max_length=8, blank=True, null=True)
	markname1 = models.CharField(max_length=254, blank=True, null=True)
	markname2 = models.CharField(max_length=254, blank=True, null=True)
	mdate = models.CharField(max_length=8, blank=True, null=True)
	address = models.CharField(max_length=254, blank=True, null=True)
	tel = models.CharField(max_length=35, blank=True, null=True)
	geom = models.PointField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'station_4326'


class VillageMoi1101007(models.Model):
	gid = models.IntegerField(primary_key=True)
	villcode = models.CharField(max_length=18, blank=True, null=True)
	countyname = models.CharField(max_length=12, blank=True, null=True)
	townname = models.CharField(max_length=12, blank=True, null=True)
	villname = models.CharField(max_length=39, blank=True, null=True)
	villeng = models.CharField(max_length=39, blank=True, null=True)
	countyid = models.CharField(max_length=3, blank=True, null=True)
	countycode = models.CharField(max_length=8, blank=True, null=True)
	townid = models.CharField(max_length=8, blank=True, null=True)
	towncode = models.CharField(max_length=12, blank=True, null=True)
	note = models.CharField(max_length=30, blank=True, null=True)
	geom = models.MultiPolygonField()

	class Meta:
		managed = False
		db_table = 'village_moi_1101007'

class MapData(models.Model):
	gid = models.IntegerField(primary_key=True)
	villcode = models.CharField(max_length=18, blank=True, null=True)
	countyname = models.CharField(max_length=12, blank=True, null=True)
	townname = models.CharField(max_length=12, blank=True, null=True)
	villname = models.CharField(max_length=39, blank=True, null=True)
	villeng = models.CharField(max_length=39, blank=True, null=True)
	countyid = models.CharField(max_length=3, blank=True, null=True)
	countycode = models.CharField(max_length=8, blank=True, null=True)
	townid = models.CharField(max_length=8, blank=True, null=True)
	towncode = models.CharField(max_length=12, blank=True, null=True)
	note = models.CharField(max_length=30, blank=True, null=True)
	geom = models.MultiPolygonField()

	class Meta:
		managed = False
		db_table = 'map_data'