from django.urls import path

from task import views

urlpatterns = [
    path("index/", views.index),
    path("pokeball/", views.pokeball),
    path("lorem/", views.lorem),
]
