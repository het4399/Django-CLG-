from django.db import models

# Create your models here.
class News(models.Model):
    Heading=models.CharField(max_length=200)
    decp=models.CharField(max_length=500)
    date=models.DateField()
    
