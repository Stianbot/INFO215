from django.shortcuts import render
from .models import Film
# Create your views here.

def film_post(request):
    movie = Film.objects.all()
    context = {
        'film_list': movie
    }

    return render(request, "filmer.html", context)