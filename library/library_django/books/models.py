from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)


class Book(models.Model):
    book_title = models.CharField(max_length=20)
    book_author = models.CharField(max_length=20)

    def __str__(self):
        return self.book_title
