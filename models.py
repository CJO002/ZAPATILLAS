from django.db import models

# Create your models here.
class SNAKERS(models.Model):

    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=60)
    color = models.CharField(max_length=100)
    talle = models.CharField(max_length=50)
    foto = models.ImageField(
        upload_to = 'foto/%Y/%m/%d',
        blank = True,
        verbose_name = ('Foto de la ZAPATILLA')
    )

class Meta:
    verbose_name = ('zapatilla')
    verbose_name_plural = ('zapatillas')

def __str__(self):
    return self.nombre