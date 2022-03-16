from statistics import mode
from unicodedata import name
from django.db import models
from django.db import connections

# Create your models here.

class CityName(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'city'
        
class AreaNames(models.Model):
    #cityNames = CityName.models.ForeignKey(id, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    city_id = models.IntegerField()
    class Meta:
        db_table = 'area'