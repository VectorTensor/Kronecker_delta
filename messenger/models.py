from django.db import models

# Create your models here.
class Messages(models.Model):
    Message=models.CharField(max_length=100)
    User=models.CharField(max_length=40)



