from django.db import models
# Create your models here.
# definir una clase de usuarios 
# parametros Usuario y password nombre y apellido

# clase de productos para mi inveentario 

class Producto(models.Model): 
    id = models.AutoField(primary_key=True)  
    title = models.CharField(max_length=100) 
    descripcion = models.TextField()
    image = models.ImageField(default='null')
    public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    
# clase de categorias para mi inventario
class Categoria(models.Model):    
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    created_at = models.DateField()
    