from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings

# Create your models here.

# Пользователи (users)
# Хранит информацию о зарегистрированных пользователях.
# Содержит логин, пароль, ФИО, email и дату регистрации.
class User(models.Model):
    login = models.CharField(unique=True, max_length=50)
    password = models.CharField(unique=True, max_length=15)
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    reg_data = models.DateTimeField(auto_now_add=True) #00-00-0000-00:00

    def __str__(self):
        return f"{self.login.title()}"

# Жанры (genres)
# Содержит список всех доступных жанров фильмов.
# Используется для классификации фильмов по категориям
# (например, "драма", "комедия", "фантастика" и т.п.).
class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name.title()}"

# Фильмы (movies)
# Хранит информацию о доступных фильмах: название, режиссёра, год выпуска и привязку к жанру.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    year_of_manufacture = models.IntegerField()
    genre_id = models.ForeignKey(
        "Genre",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.name.title()}, {self.director.title()}"

# История просмотров (watch_history)
# Логирует, какие фильмы и когда смотрел пользователь.
# Также может содержать оценку, которую пользователь поставил фильму.
class Watch_history(models.Model):

    grades = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    (None, "Unknown")
    ]

    movie_id = models.ForeignKey(
        "movie",
        on_delete=models.CASCADE,
    )
    user_id = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
    )
    viewing_date = models.DateTimeField(auto_now_add=True) #00-00-0000-00:00
    grade = models.CharField(max_length=10, choices=grades, null=True, blank=True)

    def __str__(self):
        return f"{self.user_id.login.title()} watched {self.movie_id.name.title()} at {self.viewing_date}"

# Подписки (subscriptions)
# Хранит информацию о подписках пользователей:
# тип подписки (Базовая, Стандартная, Премиум),
# даты начала и окончания.
# Привязана к пользователю.
class Subscription(models.Model):

    types = [
    ('0', 'Базовая'),
    ('1', 'Стандартная'),
    ('2', 'Премиум'),
    ]

    subscription_type = models.CharField(max_length=10, choices=types, default=('0', 'Базовая'))
    start_date = models.DateTimeField() #00-00-0000-00:00
    end_date = models.DateTimeField() #00-00-0000-00:00
    user_id = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user_id.login.title()}'s subscription"

# Платежи (payments)
# Фиксирует все совершенные платежи: сумма, дата, пользователь и за какую подписку был сделан платёж.
class Payment(models.Model):
    sum = models.FloatField()
    date_of_pay = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
    )
    subscription_id = models.ForeignKey(
        "Subscription",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"Payment from {self.date_of_pay}"
