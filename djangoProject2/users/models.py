from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    name = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Mera:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    def __str__(self):
        return self.name


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')
    ADMIN = 'admin', _('admin')


class User(AbstractUser):
    role = models.CharField(max_length=10, choices=UserRoles.choices)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    locations = models.ManyToManyField(Location)

    class Mera:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

    # def save(self, *args, **kwargs):
    #     self.set_password(self.password)
    #     super().save(*args, **kwargs)
