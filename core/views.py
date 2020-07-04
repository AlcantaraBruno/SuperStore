from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

# Create your views here.

#segurança para não acessar a pagina autenficada pelo link
@login_required(login_url='/login/')
def index(request):
    return render(request, 'index.html')

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