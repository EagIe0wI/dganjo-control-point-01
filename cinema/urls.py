from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import MovieCreateView, MovieUpdateView

urlpatterns = [
    path('', views.index, name='index'),
    path("accounts/login/", auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("logout/", views.logout_view, name='logout'),
    path("movies/movie-<int:movie_id>/", views.detail, name="detail"),
    path("movies/movie-<int:movie_id>/delete/", views.delete, name="delete"),
    path("movies/", views.movies_list, name="movies_list"),
    path("movies/add/", MovieCreateView.as_view(), name="movie_form"),
    path("movies/movie-<int:pk>/update/", MovieUpdateView.as_view(), name="movie_form"),
]
