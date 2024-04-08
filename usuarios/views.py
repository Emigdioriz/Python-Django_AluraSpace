from django.shortcuts import render, redirect

from usuarios.forms import LoginForms, CadastroForms

from django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.
def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            nome_login = form["nome_login"].value()
            senha = form["senha"].value()

            usuario = auth.authenticate(request, username=nome_login, password=senha)
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'{nome_login} logado com sucesso')
                return redirect('index')
            else:
                messages.error(request, 'Usuário ou senha inválidos')
                return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            if form["senha"].value() != form["senha2"].value():
                messages.error(request, 'As senhas não são iguais')
                return redirect('cadastro')
            
            nome = form["nome"].value()
            email = form["email"].value()
            senha = form["senha"].value()

            if User.objects.filter(username = nome).exists():
                messages.error(request, 'Usuário já existe')
                return redirect('cadastro')
            
            usuario = User.objects.create_user(nome, email, senha) 
            usuario.save()
            messages.success(request, f'{nome} cadastrado com sucesso')
            return redirect('login')
    
    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Deslogado com sucesso')
    return redirect('login')