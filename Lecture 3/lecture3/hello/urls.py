from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("person", views.person, name = "person"),
    path("<str:name>", views.greet, name = "greet"),
]