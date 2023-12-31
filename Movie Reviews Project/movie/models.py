from django.db import models

# Create your models here

class Movie(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    url=models.URLField(blank=True)
    image=models.ImageField(upload_to='movie/images')