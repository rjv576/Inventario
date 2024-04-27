from django.db import models

# Create your models here.
# definir una clase de usuarios 
# parametros Usuario y password nombre y apellido

class Usuario(models.Model):    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    
# clase de productos para mi inveentario 

class Producto(models.Model):   
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    
    