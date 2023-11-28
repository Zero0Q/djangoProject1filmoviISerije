from django.shortcuts import render, get_object_or_404
from .models import Film


# Create your views here.
def home(request):

    context = {

    }
    return render(request, 'home.html', context)


def filmovi(request):
    queryset = Film.objects.all()

    context = {
        'filmovi': queryset
    }
    return render(request, 'filmovi.html', context)





def detail_look(request, id):

    obj = get_object_or_404(Film, id=id)

    context = {
        'object': obj
    }
    return render(request, 'film_detail.html', context)
