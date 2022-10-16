from django.db import models

# Create your models here.
class brand(models.Model):
    name = models.CharField(max_length=255)
    emissions = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='images')
