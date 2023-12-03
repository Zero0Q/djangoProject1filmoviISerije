from django.shortcuts import render
from .models import Galerija

# Create your views here.
def slike(request):

    foto = Galerija.objects.all()

    context = {
        'foto': foto
    }
    return render(request, 'slike.html', context)
