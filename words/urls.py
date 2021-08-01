from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("random_words", views.rand_words),
    path("reset", views.reset),
    path("login/<name>", views.login),
]
