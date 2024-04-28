from django.db import models

# Create your models here.
class UploadImage(models.Model):
    image = models.ImageField(upload_to='photos/')
    title = models.CharField(max_length=200, default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.title
    
     