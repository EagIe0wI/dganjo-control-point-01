from django.db import models

# Create your models here.

class User(models.Model):
    fio = models.CharField(max_length=50, null=True, blank=True)
    login = models.CharField(unique=True, max_length=50)
    reg_data = models.DateTimeField(auto_now_add=True) #00-00-0000-00:00

    def __str__(self):
        return f"{self.fio.title()}"