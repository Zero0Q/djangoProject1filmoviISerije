from django.urls import path
from .views import home, detail_look, filmovi

# app_name = 'filmovi'

urlpatterns = [
    path('', home, name='home'),

    path('filmovi/', filmovi, name='filmovi'),

    path('filmovi/<int:id>/', detail_look, name='film-detail'),

]