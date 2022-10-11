from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.charField()
    description = models.Textfield()
    quantity = models.IntegerField()
    
