from django.urls import path
from . import views

urlpatterns = [
    path('', views.coming_soom, name='coming_soon'),
]
