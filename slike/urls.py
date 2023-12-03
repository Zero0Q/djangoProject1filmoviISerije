from django.urls import path
from .views import slike

# app_name = 'slike'

urlpatterns = [
    path('', slike, name='slike'),
]
