from django.shortcuts import render
from .models import Serija

# Create your views here.
def serije(request):

    queryset = Serija.objects.all()

    context = {
        'serije': queryset
    }
    return render(request, 'serije.html', context)




