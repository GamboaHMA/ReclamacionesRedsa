from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, ReclamationForm
from .models import Reclamacion
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'users/log.html', {'form': form})
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'users/home.html', {'form': form})
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def home(request):
    
    return render(request, '../../users/home.html')

@login_required
def nueva_reclamacion(request):
    if request.method == 'POST':
        form = ReclamationForm(request, data=request.POST)
        if form.is_valid:
            reclamacion = form.save(commit=False)
            reclamacion.usuario = request.user
            reclamacion.save()
            messages.success(request, 'Reclamacion creada con exito')
            return redirect('../')
    else:
        form = ReclamationForm()
    return render(request, 'nueva_reclamacion.html', {'form': form})