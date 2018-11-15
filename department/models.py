from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import math
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=32,)
    location = models.CharField(max_length=128, blank=True)
    latitude = models.FloatField(blank=True, null=True, default=0,validators=[MaxValueValidator(90), MinValueValidator(-90)])
    longitude = models.FloatField(blank=True, null=True, default=0,validators=[MaxValueValidator(180), MinValueValidator(-180)])

    def __str__(self):
        return str(self.id) + ' (' + self.name + ')'

    def save(self, **kwargs):
	    super(Department, self).save(**kwargs)
	    if self.latitude and self.longitude:
	    	from distance.models import Distance
	    	from housing.models import House
	        house_set = House.objects.raw('SELECT * FROM housing_house WHERE latitude IS NOT NULL and longitude IS NOT NULL')
	        for house_item in house_set:
	            gap = math.sqrt((self.latitude - house_item.latitude)*(self.latitude - house_item.latitude) + (self.longitude - house_item.longitude)*(self.longitude - house_item.longitude))
	            distance = Distance(house_id = house_item, department_id = self, distance = gap)
	            distance.save()    
	 
