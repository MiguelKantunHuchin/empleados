from django.contrib import admin
from django.urls import path
from . import views

app_name = "departamento_app"
urlpatterns = [
    path("new-departamento", views.NewDepartamento.as_view(), name='nuevo_depa'),
    path("lista-departamentos", views.DepartamentoListView.as_view(), name="lista_all"),
]
