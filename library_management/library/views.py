from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import Book, AdminUser
from .serializers import BookSerializer, AdminSerializer

# Admin Signup
class AdminSignupView(generics.CreateAPIView):
    queryset = AdminUser.objects.all()
    serializer_class = AdminSerializer

    def get(self, request, *args, **kwargs):
        return Response({"message": "Use POST to sign up"}, status=status.HTTP_200_OK)
                        
    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()
        Token.objects.create(user=user)

# Admin Login
class AdminLoginView(generics.GenericAPIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=email, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

# CRUD operations for books
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Book, AdminUser

# Student View - List All Books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

# Admin Signup
def admin_signup(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        if not AdminUser.objects.filter(email=email).exists():
            user = AdminUser.objects.create_user(email=email, password=password)
            login(request, user)
            return redirect("add_book")
    return render(request, "books/signup.html")

# Admin Login
def admin_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return redirect("add_book")
    return render(request, "books/login.html")

# Admin - Add a Book
def add_book(request):
    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        published_date = request.POST["published_date"]
        isbn = request.POST["isbn"]
        Book.objects.create(title=title, author=author, published_date=published_date, isbn=isbn)
        return redirect("book_list")
    return render(request, "books/add_book.html")
