from django.contrib import admin
from .models import AdminUser, Book

# Register the models
admin.site.register(AdminUser)
admin.site.register(Book)
