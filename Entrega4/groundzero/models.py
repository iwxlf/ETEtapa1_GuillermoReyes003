from django.db import models

# Create your models here.
class TipoMoneda(models.Model):
    idMoneda = models.IntegerField(primary_key=True, verbose_name='Id moneda')
    nombreMoneda = models.CharField(max_length=50, verbose_name='Nombre moneda')

    def __str__(self):
        return self.nombreMoneda


class Contacto(models.Model):
    numero_identificaion = models.CharField(max_length=20, primary_key=True, verbose_name='Numero de Identificacion')
    nombre_completo = models.CharField(max_length=50, verbose_name='Nombre completo')
    telefono = models.CharField(max_length=15, verbose_name='Telefono')
    direccion = models.CharField(max_length=50, verbose_name='direccion')
    email = models.CharField(max_length=20, verbose_name='Email')
    pais = models.CharField(max_length=20, verbose_name='Pais')
    contraseña = models.CharField(max_length=20, verbose_name='Constraseña')
    moneda = models.ForeignKey(TipoMoneda, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_identificaion