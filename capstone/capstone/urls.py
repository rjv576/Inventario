"""
URL configuration for capstone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('create-product/', views.create_product, name='create-product'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('register/', views.register_page, name='register'),
    path('login/', views.loging_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('inventory/', views.inventory_page, name='inventory'),
    path('edit-product/<int:id>/', views.edit_product, name='edit-product'),
    path('delete-product/<int:id>/', views.delete_product, name='delete-product'),
    
  
]

# Ruta imagenes

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)