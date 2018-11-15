from django.db import models
from provider.models import Provider
import provider.models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from math import *

# Create your models here.

class House(models.Model):
    name = models.CharField(max_length=32,)
    location = models.CharField(max_length=128, blank=True)
    price = models.IntegerField(default=0)
    cover_img = models.CharField(max_length=128, blank=True, default='')
    types = models.CharField(max_length=32, blank=True)
    description = models.CharField(max_length=600, blank=True)
    provider = models.ForeignKey(Provider, blank=True, null=True)
    imgs_url = ArrayField(models.CharField(max_length=128, blank=True), size=100, default=[], blank=True)
    latitude = models.FloatField(blank=True, null=True, default=0,validators=[MaxValueValidator(90), MinValueValidator(-90)])
    longitude = models.FloatField(blank=True, null=True, default=0,validators=[MaxValueValidator(180), MinValueValidator(-180)])

    def __str__(self):
        return str(self.id) + ' (' + self.name + ')'
    
    def save(self, **kwargs):
        from distance.models import Distance
        from department.models import Department
        super(House, self).save(**kwargs)
        if self.latitude and self.longitude:
            department_set = Department.objects.raw('SELECT * FROM department_department WHERE latitude IS NOT NULL and longitude IS NOT NULL')
            for department_item in department_set:
                gap = sqrt((self.latitude - department_item.latitude)*(self.latitude - department_item.latitude) + (self.longitude - department_item.longitude)*(self.longitude - department_item.longitude))
                distance = Distance(house_id = self, department_id=department_item, distance=gap)
                distance.save()

    
