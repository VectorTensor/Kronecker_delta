from django.db import models

# Create your models here.
class Questions(models.Model):
    Question=models.CharField(max_length=200)
    Answer=models.CharField(max_length=40)


    
