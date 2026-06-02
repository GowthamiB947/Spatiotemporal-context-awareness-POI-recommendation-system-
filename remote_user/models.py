from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)


class predict_poi_recommendation(models.Model):

    pid= models.CharField(max_length=300)
    point_name= models.CharField(max_length=300)
    latitude_radian= models.CharField(max_length=300)
    longitude_radian= models.CharField(max_length=300)
    num_links= models.CharField(max_length=300)
    point_links= models.CharField(max_length=300)
    num_categories= models.CharField(max_length=300)
    categories= models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



