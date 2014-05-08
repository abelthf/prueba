from django.db import models

# Create your models here.
class Producto(model.Models):
    nombre = model.CharField(max_length=255)
