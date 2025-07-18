from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    marks=models.FloatField()
    address=models.TextField()


class movie(models.Model):
    name=models.CharField(max_length=50)
    reviews=models.IntegerField()
    rel_date=models.DateField()