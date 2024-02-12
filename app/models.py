from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=2080)
    department=models.CharField(max_length=2080)
    dob=models.DateField()
    address=models.CharField(max_length=2080)
    others=models.TextField()
    gender=models.CharField(max_length=2080,default="male")
