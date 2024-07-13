from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Reclamacion

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ReclamationForm(forms.ModelForm):
    class Meta:
        model = Reclamacion
        fields = ['banco', 
                'canal_pago',
                'fecha_operacion', 
                'tarjeta', 'traza', 
                'autorizo_operacion', 
                'numero_referencia', 
                'importe_operacion', 
                'importe_reclamacion', 
                'motivo_reclamacion']