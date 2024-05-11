from django.db import models
# Create your models here.
# definir una clase de usuarios 
# parametros Usuario y password nombre y apellido

# clase de productos para mi inveentario 
from PIL import Image
class Producto(models.Model): 
    id = models.AutoField(primary_key=True)  
    title = models.CharField(max_length=100) 
    descripcion = models.TextField()
    image = models.ImageField(blank=True,null=True,verbose_name='Imagen',upload_to='media')
    public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
def save(self, *args, **kwargs): # Redefinir el metodo save
    super(Producto, self).save(*args, **kwargs) # Llamar al metodo save de la clase padre

    if self.image: # Si la imagen existe
        img = Image.open(self.image.path) # Abrir la imagen
        if img.height > 300 or img.width > 300: # Si la imagen es mayor a 300px
            output_size = (300, 300) # Tamaño de salida
            img.thumbnail(output_size) # Redimensionar la imagen
            img.save(self.image.path) # Guardar la imagen redimensionada
  
