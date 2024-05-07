from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponseForbidden
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
            messages.success(request, 'Login successful. Welcome back!')
            return redirect('products')
            
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request,'users/login.html',
    {
        'title': 'Login'
    })
# vista de contacto
def contact(request):
    """
    This function handles the contact view.
    """
  
    return render(request,'contact.html')
# vista de about
def about(request):
    """
    This function handles the about view.
    """
    return render(request,'about.html')


# Editar un producto
@login_required(login_url='login') # Redirect to the login page if the user is not logged in
def edit_product(request, id): # request and the product ID
    if not request.user.is_staff and not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to perform this action")
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.title = request.POST.get('title')
        producto.descripcion = request.POST.get('descripcion')
        image = request.FILES.get('image') # Get the image from the request
        if image : 
            producto.image = image
        public = 'public' in request.POST # Check if the product is public
        producto.public = public
        producto.save()
        messages.success(request, "Product updated successfully.")
        return redirect(reverse('products'))
    return render(request, 'inventory/edit_product.html', {
        'producto': producto
    })  
# Crear Producto
@login_required(login_url='login') # Redirect to the login page if the user is not logged in
def create_product(request):
    if not request.user.is_staff and not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to perform this action")
    if request.method == 'POST':
        title = request.POST.get('title')
        descripcion = request.POST.get('descripcion')
        image = request.FILES.get('image') # Get the image from the request
        public = 'public' in request.POST # Check if the product is public
        producto = Producto.objects.create(title=title, descripcion=descripcion,image=image, public=public)
        if image: # Check if there is an image in the request
            producto.image = image
            producto.save()
        messages.success(request, "Successfully created product.")
        return redirect(reverse('products'))
    return render(request, 'inventory/create_product.html')

# eliminar un producto
@login_required(login_url='login') # Redirect to the login page if the user is not logged in
def delete_product(request, id_producto):
    if not request.user.is_staff and not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to perform this action")
    producto = Producto.objects.get(id=id_producto)
    producto.delete()
    messages.success(request, "Product deleted successfully.")
    return redirect(reverse('products'))

# listar productos
@login_required(login_url='login') # Redirect to the login page if the user is not logged in
def products(request): 
    search_query = request.GET.get('search', '')
    if search_query:
        productos = Producto.objects.filter(Q(title__icontains=search_query) | Q(descripcion__icontains=search_query))
    else:
        productos = Producto.objects.all()
    
    return render(request,'inventory/productos.html', {
        'productos': productos
    })
    

def is_superuser_check(user): # Function to check if a user is a superuser
    return user.is_superuser

@user_passes_test(is_superuser_check) # Only superusers can access this view
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

# vista de inventario   
@login_required(login_url='login') # Redirect to the login page if the user is not logged in
def inventory_page(request):
    """
    This function handles the inventory view.
    """
    return render(request,'inventory/inventory.html')
# vista de logout
def logout_user(request):
    logout(request)
    return redirect('login')