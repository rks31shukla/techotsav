from django.db import models
from django.db.models.fields import PositiveBigIntegerField

# Create your models here.
class Registrations(models.Model):
    Name = models.CharField(max_length=70)
    Branch = models.CharField(max_length=50)
    Year = models.IntegerField()
    Section =models.CharField(max_length=3)
    Email =models.EmailField(max_length=254)
    Contact_No = models.PositiveBigIntegerField()
    Roll=models.PositiveBigIntegerField(default=1)
    Contest = models.CharField(max_length=200)
