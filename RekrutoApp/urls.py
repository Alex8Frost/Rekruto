from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_text),
    path('', views.print_text, name='hello')
]