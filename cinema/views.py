from django.shortcuts import get_object_or_404, render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
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

def delete(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == "POST":
        movie.delete()
        return redirect('/movies/')

    return render(request, "cinema/delete.html", {"movie": movie})

def login(request):
    context = {
        'title': 'Django Login',
        'message': 'This is Login',
    }

    return render(request, 'home.html' ,context)

def logout_view(request):
    logout(request)
    return redirect('index')

class MovieCreateView(CreateView):
    model = Movie
    fields = "__all__"
    success_url = "/movies/"

class MovieUpdateView(UpdateView):
    model = Movie
    fields = "__all__"
    success_url = "/movies/"

