from django.urls import path
from . import views

urlpatterns = [
    path('traits/', views.TraitViews.as_view()),
]