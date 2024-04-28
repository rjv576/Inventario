from django.contrib import admin

# Register your models here.
# registra mis modelos en el admin
from .models import  Producto
admin.site.register(Producto)