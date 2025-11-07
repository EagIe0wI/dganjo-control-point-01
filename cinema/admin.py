from django.contrib import admin
from .models import User, Genre, Movie, Watch_history, Subscription, Payment

# Register your models here.

admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Watch_history)
admin.site.register(Subscription)
admin.site.register(Payment)
