from django.db import models

# Create your models here.

class Product(models.Model):
  name = models.CharField(max_length=120)
  image = models.ImageField(upload_to='products',default='No_Picture.png')
  prize = models.FloatField(help_text='in US dollars $')
  createdDate = models.DateTimeField(auto_now_add=True)
  updatedDate = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return f"{self.name}-{self.createdDate.strftime('%d/%m/%Y')}"