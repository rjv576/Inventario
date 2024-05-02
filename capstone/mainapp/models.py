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
    image = models.ImageField(blank=True,null=True,verbose_name='Imagen',upload_to='products/')
    public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.

        img = Image.open(self.image.path)  # Open the image file.

        if img.height > 300 or img.width > 300:  # If the image is larger than 300x300 pixels...
            output_size = (300, 300)  # Set the new size.
            img.thumbnail(output_size)  # Resize the image.
            img.save(self.image.path)  # Save the image back to the same path.
  
