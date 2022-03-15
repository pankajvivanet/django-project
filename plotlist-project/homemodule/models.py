from django.db import models
from django.db import connections

# Create your models here.

class CityName(models.Model):
    name = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'city'
        
class AreaNames(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    city_id = models.IntegerField()
    
    class Meta:
        db_table = 'area'