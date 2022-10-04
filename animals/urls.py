from django.urls import path
from . import views

urlpatterns = [
    path('animals/', views.AnimalViews.as_view()),
]