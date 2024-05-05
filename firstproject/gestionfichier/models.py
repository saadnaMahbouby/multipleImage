from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

 
class Annonce(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class UploadImage(models.Model):
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE, default=1)  # Remplacez 1 par l'ID de l'annonce par défaut si nécessaire
    image = models.ImageField(upload_to='photos/')


