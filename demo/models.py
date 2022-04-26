from django.db import models
from django.urls import reverse
# Create your models here.
class emp(models.Model):
    my_field = models.BooleanField(default=True)
    blog_views=models.IntegerField(default=0)
    name = models.CharField(max_length=100,null=True,blank=True)
    DOB= models.CharField(null=True,blank=True,max_length=100)
    DOJ= models.CharField(null=True,blank=True,max_length=100)
    Department= models.CharField(max_length=100,null=True,blank=True)
    post= models.CharField(max_length=100,null=True,blank=True)
    Adress= models.CharField(max_length=100,null=True,blank=True)
    City=models.CharField(max_length=100,null=True,blank=True)
    Country=models.CharField(max_length=100,null=True,blank=True)
   
