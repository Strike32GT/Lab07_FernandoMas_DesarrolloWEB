from django import forms
from .models import Usuario,Evento,RegistroEvento

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=['nombre','email']


class EventoForm(forms.ModelForm):
    class Meta:
        model=Evento
        fields=['titulo','descripcion','fecha','lugar','organizador']


class RegistroEventoForm(forms.ModelForm):
    class Meta:
        model=RegistroEvento
        fields=['usuario','evento']