from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .models import Product
# Create your views here.

#segurança para não acessar a pagina autenficada pelo link

@login_required(login_url='/login/')
def register_product (request):
    return render(request, 'register-product.html')

def set_product (request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    price = request.POST.get('price')
    photo = request.FILES.get('file')
    user = request.user
    product = Product.objects.create(name=name, description=description, price=price,photo=photo, user=user)

    url = '/store/detail/{}'.format(product.id)
    return redirect (url)

def delete_product (request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/')

@login_required(login_url='/login/')
def list_all_store(request):
    product = Product.objects.filter(active=True)
    print(product.query)
    return render(request, 'list.html', {'product': product})

def list_user_store(request):
    product = Product.objects.filter(active=True, user=request.user)
    return render(request, 'list.html', {'product': product})

def store_detail (request, id):
    product = Product.objects.get(active=True, id=id)
    print(product.id)
    return render(request, 'product.html', {'product': product})

#Permitir que o usario saia da conta
def logout_user(request):
    logout(request)
    return redirect('/login/')

#redericionamento para página de login
def login_user (request):
    return render (request, 'login.html')

#autentificação de login e senha
@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password= password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválido. Favor tentar novamente.')
    return redirect('/login/')