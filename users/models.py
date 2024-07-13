from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Reclamacion(models.Model):
    ESTADO_RECLAMACION = [
        ('registrada', 'Registrada'),
        ('espera_banco', 'En espera de respuesta del banco'),
        ('espera_remesador', 'En espera de respuesta del remesador'),
        ('procesada', 'Procesada'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    banco = models.CharField(max_length=100)
    canal_pago = models.CharField(max_length=100)
    fecha_operacion = models.DateField()
    tarjeta = models.CharField(max_length=100)
    traza = models.CharField(max_length=100)
    autorizo_operacion = models.CharField(max_length=100)
    numero_referencia = models.CharField(max_length=100)
    importe_operacion = models.DecimalField(max_digits=10, decimal_places=2)
    importe_reclamacion = models.DecimalField(max_digits=10, decimal_places=2)
    motivo_reclamacion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADO_RECLAMACION, default='registrada')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reclamación {self.id} - {self.banco}"