from django.urls import path
from . import views

urlpatterns = [
    path('groups/', views.GroupViews.as_view()),
]