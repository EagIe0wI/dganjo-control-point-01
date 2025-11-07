from django.shortcuts import get_object_or_404, render
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Movie

# Create your views here.

def index(request):
    context = {
        'title': 'Django Index',
        'message': 'This is Index',
    }

    return render(request, 'index.html' ,context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, "detail.html", {"movie": movie})

def movies_list(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, "list.html", context)

def login(request):
    context = {
        'title': 'Django Login',
        'message': 'This is Login',
    }

    return render(request, 'home.html' ,context)

def logout_view(request):
    logout(request)
    return redirect('index')
