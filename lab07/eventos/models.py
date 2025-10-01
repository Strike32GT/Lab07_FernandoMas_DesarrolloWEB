from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre=models.CharField(max_length=200)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.nombre
    
class Evento(models.Model):
    titulo=models.CharField(max_length=100,unique=True)
    descripcion=models.TextField()
    fecha=models.DateField()
    lugar=models.CharField(max_length=200)
    organizador=models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='eventos_organizados')


    def __str__(self):
        return self.titulo

class RegistroEvento(models.Model):
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='registros')
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='registros')
    fecha_registro=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.nombre} - {self.evento.titulo}"        