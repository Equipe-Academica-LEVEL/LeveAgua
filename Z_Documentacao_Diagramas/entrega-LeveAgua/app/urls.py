from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("criar/", views.criar, name="criar"),
    path("", views.listarTudo, name="listar"),
    path("editar/<int:id_app>", views.editar, name="atualizar"),
    path("deletar/<int:id_app>", views.deletar, name="deletar"),
    path("detail/<int:id_app>", views.detail, name="detail"),
    path("deletar/delete/<int:id_app>", views.delete, name="deletar"),
]
