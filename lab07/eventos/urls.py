from django.urls import path
from . import views

urlpatterns=[
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/nuevo/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),

    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('eventos/nuevo/', views.crear_evento, name='crear_evento'),
    path('eventos/editar/<int:pk>/', views.editar_evento, name='editar_evento'),
    path('eventos/eliminar/<int:pk>/', views.eliminar_evento, name='eliminar_evento'),

    path('registros/', views.lista_registros, name='lista_registros'),
    path('registros/nuevo/', views.crear_registro, name='crear_registro'),
    path('registros/eliminar/<int:pk>/', views.eliminar_registro, name='eliminar_registro'),

    path('consultas/', views.consultas, name='consultas'),
]