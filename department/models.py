from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import math
from assist import *
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=32,)
    location = models.CharField(max_length=128, blank=True)
    latitude = models.FloatField(blank=True, null=True, default=0,validators=[MaxValueValidator(90), MinValueValidator(-90)])
    longitude = models.FloatField(blank=True, null=True, default=0,validators=[MaxValueValidator(180), MinValueValidator(-180)])

    def __str__(self):
        return str(self.id) + ' (' + self.name + ')'

    def save(self, **kwargs):
		super(Department,self).save(**kwargs)
		from distance.models import Distance
		from housing.models import House
		if self.latitude != 0 or self.longitude != 0:
			distance_set = Distance.objects.raw('SELECT * FROM distance_distance WHERE department_id_id = %s',[self.pk])
			for distance_item in distance_set:
				house_item = distance_item.house_id
				new_distance = getSphereDistance(lat1=self.latitude, lon1=self.longitude, lat2=house_item.latitude, lon2=house_item.longitude)
				distance_item.distance = new_distance
				distance_item.save()
			house_set = House.objects.raw('SELECT * FROM housing_house WHERE (housing_house.latitude <> 0 OR housing_house.longitude <> 0) AND housing_house.id NOT IN (SELECT house_id_id FROM distance_distance WHERE department_id_id = %s)', [self.pk])
			for house_item in house_set:
				gap = getSphereDistance(lat1=self.latitude, lon1=self.longitude, lat2=house_item.latitude, lon2=house_item.longitude)
				distance = Distance(house_id=house_item, department_id=self, distance=gap)
				distance.save()