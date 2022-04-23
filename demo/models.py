from django.db import models
from django.urls import reverse
# Create your models here.
class emp(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    DOB= models.IntegerField(null=True,blank=True)
    DOJ= models.IntegerField(null=True,blank=True)
    Department= models.CharField(max_length=100,null=True,blank=True)
    post= models.CharField(max_length=100,null=True,blank=True)
    Adress= models.CharField(max_length=100,null=True,blank=True)
    City=models.CharField(max_length=100,null=True,blank=True)
    Country=models.CharField(max_length=100,null=True,blank=True)
