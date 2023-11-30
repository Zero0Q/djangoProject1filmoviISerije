from django.urls import path
from .views import serije, serija_detail

app_name = 'serije'

urlpatterns = [
    path('', serije, name='serije'),

    path('<int:id>/', serija_detail, name='serija_detail'),


]