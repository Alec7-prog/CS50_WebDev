from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry, name="entry"),
    path('search/', views.search, name="search"),
    path("create/", views.createEntry, name="createEntry"),
    path("edit/<str:title>", views.edit, name="edit"), 
    path("random/", views.randomGenerator, name="random")
]
