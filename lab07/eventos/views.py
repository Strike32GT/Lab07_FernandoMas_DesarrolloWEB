from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Count
from .models import Usuario,Evento,RegistroEvento
from .forms import UsuarioForm,EventoForm,RegistroEventoForm

# Create your views here.

#CRUD para usuarios
def lista_usuarios(request):
    usuarios=Usuario.objects.all()
    return render(request,'eventos/lista_usuarios.html',{'usuarios':usuarios})

def crear_usuario(request):
    if request.method=="POST":
        form=UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
        
    else:
        form=UsuarioForm()
    return render(request, 'eventos/form_usuario.html',{'form':form})        
        
def editar_usuario(request,pk):
    usuario=get_object_or_404(Usuario,pk=pk)
    if request.method=="POST":
        form=UsuarioForm(request.POST,instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form=UsuarioForm(instance=usuario)
    return render(request, 'eventos/form_usuario.html',{"form":form})


def eliminar_usuario(request,pk):
    usuario=get_object_or_404(Usuario,pk=pk)
    usuario.delete()
    return redirect('lista_usuarios')
        

#CRUD DE EVENTOS
def lista_eventos(request):
    eventos=Evento.objects.all()
    return render(request,'eventos/lista_eventos.html',{'eventos':eventos})

def crear_evento(request):
    if request.method=="POST":
        form=EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form=EventoForm()
    return render(request, 'eventos/form_evento.html',{'form':form})
        
def editar_evento(request,pk):
    evento=get_object_or_404(Evento,pk=pk)
    if request.method=="POST":
        form=EventoForm(request.POST,instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form=EventoForm(instance=evento)
    return render(request, 'eventos/form_evento.html',{"form":form})


def eliminar_evento(request,pk):
    evento=get_object_or_404(Evento,pk=pk)
    evento.delete()
    return redirect('lista_eventos')



#CRUD REGISTRO EVENTO
def lista_registros(request):
    registros=RegistroEvento.objects.all()
    return render(request,'eventos/lista_registros.html',{'registros':registros})


def crear_registro(request):
    if request.method=="POST":
        form=RegistroEventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_registros')
    else:
        form=RegistroEventoForm()
    return render(request, 'eventos/form_registro.html',{"form":form})        


def eliminar_registro(request,pk):
    registro=get_object_or_404(RegistroEvento,pk=pk)
    registro.delete()
    return redirect('lista_registros')



#Consulta Avanzada
def consultas(request):
    usuarios_activos=Usuario.objects.annotate(num_eventos=Count('registros')).order_by('-num_eventos')[:5]
    eventos_mes=Evento.objects.filter(fecha__month=1)
    return render(request, 'eventos/consultas.html',{
        'usuarios_activos':usuarios_activos,
        'eventos_mes':eventos_mes,
    })
