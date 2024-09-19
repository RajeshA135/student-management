
from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=25,blank=False,null=False)
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=25,blank=False,null=False)
    branch=models.CharField(max_length=25,blank=False,null=False,default='Unknown')
    
    def __str__(self):
        return self.name