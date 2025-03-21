from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class AdminUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = None  

    # Add related_name to avoid conflicts
    groups = models.ManyToManyField(Group, related_name="admin_users", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="admin_users_permissions", blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
