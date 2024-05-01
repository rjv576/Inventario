from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Producto
from .forms import RegistrationForm


# Create your views here.

def index(request):
    return render(request,'index.html')


# vista del login request
def loging_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('inventory')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request,'users/login.html',
    {
        'title': 'Login'
    })

def contact(request):
    """
    This function handles the contact view.
    """
  
    return render(request,'contact.html')

def about(request):
    """
    This function handles the about view.
    """
    return render(request,'about.html')


def create_product(request):
    """
    This function handles the create_product view.
    """
    producto = Producto(
        title = 'Primer Producto',
        descripcion = 'Este es el primer producto de la tienda',
        public = True,
        
    )
    producto.save()
    return HttpResponse(f'Producto {producto.title} creado exitosamente')

# Editar un producto
def edit_product(request, id):
    """
    This function handles the edit_product view.
    """
    producto = Producto.objects.get(pk=id) # Get the product by its id
    producto.title = 'Producto editado' # Change the title of the product
    producto.descripcion = 'Este producto ha sido editado' # Change the description of the product
    producto.save()
    return HttpResponse(f'Producto {producto.title} editado exitosamente')

# eliminar un producto
def delete_product(request, id):
    """
    This function handles the delete_product view.
    """
    producto = Producto.objects.get(pk=id)
    producto.delete()
    return redirect('products')

# listar productos
def products(request): 
    productos = Producto.objects.all()
    
    return render(request,'inventory/productos.html', {
        'productos': productos
    })


def is_superuser_check(user):
    return user.is_superuser

@user_passes_test(is_superuser_check)
def register_page(request):
    register_form = RegistrationForm()
    
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            messages.success(request, 'Account created successfully')
            register_form.save() # Save the user to the database
            return redirect('home')
        else:
            print(register_form.errors) # Print the errors to the console
        
    return render(request, 'users/register.html', {
        'title': 'Register',
        'register_form': register_form
    })
    
@login_required(login_url='login')
def inventory_page(request):
    """
    This function handles the inventory view.
    """
    return render(request,'inventory/inventory.html')
def logout_user(request):
    logout(request)
    return redirect('login')