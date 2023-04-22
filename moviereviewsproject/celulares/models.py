from django.db import models

class Celulares(models.Model):
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.modelo
