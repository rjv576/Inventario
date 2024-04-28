from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Producto
from .forms import RegistrationForm

# Create your views here.

def index(request):
    return render(request,'index.html')


# login view
def login_view(request):
    """
    This function handles the login view.
    """
    return render(request,'login.html')

# vista del login request
def login_request(request):
    """
    This function handles the login functionality.
    """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user=user)  # Modified function call
            return redirect('products/')
        # Removed unnecessary else statement and de-indented the code inside it
        # In case of authentication failure, you can handle it here
    return render(request, 'login.html')

def contact(request, nombre="", apellidos="", correo=""):
    """
    This function handles the contact view.
    """
    context = {
        'name': nombre,
        'lastname': apellidos,
        'email' : correo,
    }
    return render(request,'contact.html', context)

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


def products(request):
    """
    This function handles the products view.
    """
    
    producto = Producto.objects.get(pk=1)
    
    return HttpResponse(f"Producto: {producto.title} - Descripción: {producto.descripcion}")


def register_page(request):
    register_form = RegistrationForm()
    
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save() # Save the user to the database
            return redirect('home')
        else:
            print(register_form.errors) # Print the errors to the console
        
    return render(request, 'users/register.html', {
        'register_form': register_form
    })
