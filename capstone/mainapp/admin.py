from django.contrib import admin

# Register your models here.
# registra mis modelos en el admin
from .models import  Producto
admin.site.register(Producto)

# configuracion del panel de administracion
title = "Capstone Project"
subtitle = "Administrative Page"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle