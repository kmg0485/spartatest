from django.urls import path
from . import views

urlpatterns = [
    path('introduce/', views.first_view, name='first_view'),
]