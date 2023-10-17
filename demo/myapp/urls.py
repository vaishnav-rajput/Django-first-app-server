from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), #connected to home function in views
    path("todos/", views.todos, name="Todos")
]