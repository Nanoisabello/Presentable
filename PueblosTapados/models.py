from django.db import models

class Pueblos (models.Model):
    nombre= models.TextField(max_length=100)
    Provincia= models.TextField(max_length=100)
    creado_el= models.DateTimeField(auto_now_add=True)
    modificado_el=models.DateTimeField(auto_now=True)

def __str__(self):
     return f"{self.id} / {self.nombre} / {self.estado} / {self.creado_el}"
    
class usuarios (models.Model):
    nombre = models.TextField(max_length=100)
    apellido = models.TextField(max_length=100)
    email = models.EmailField

def __str__(self):
    return f"{self.id}, {self.nombre},{self.apellido}, {self.fecha_nacimiento}"
    