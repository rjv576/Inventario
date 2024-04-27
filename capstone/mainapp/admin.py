from django.contrib import admin

# Register your models here.
# registra mis modelos en el admin
from .models import Usuario, Producto
admin.site.register(Usuario)
admin.site.register(Producto)