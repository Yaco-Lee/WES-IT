from django.db import models

class Persona(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    nombre = models.TextField(max_length=500, blank=False)
    apellido = models.TextField(max_length=500, blank=False)
    dni = models.PositiveIntegerField(default=0)
    fecha_nac = models.DateField(blank=False)

