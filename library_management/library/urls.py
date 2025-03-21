from django.urls import path
from .views import AdminSignupView, BookListCreateView

urlpatterns = [
    path('admin/signup/', AdminSignupView.as_view(), name='admin-signup'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
]

from django.urls import path
from .views import book_list, admin_signup, admin_login, add_book

urlpatterns = [
    path("", book_list, name="book_list"),  
    path("signup/", admin_signup, name="admin_signup"),
    path("login/", admin_login, name="admin_login"),
    path("add-book/", add_book, name="add_book"),
]
