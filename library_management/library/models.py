from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class AdminUser(AbstractUser):
    class Meta:
        app_label = 'library'

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="admin_users",  # Custom related_name to avoid conflict
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="admin_users_permissions",  # Custom related_name to avoid conflict
        blank=True,
    )

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
