from datetime import timezone
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Book, LibraryUser, Transaction
from .serializers import BookSerializer, LibraryUserSerializer, TransactionSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('available_books')  # Redirect to the book list or another page
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid login details.")
    
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

# Existing BookViewSet for authenticated users (CRUD)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

# Custom View for showing all available books (accessible without login)
class BookListView(APIView):
    permission_classes = [AllowAny]  # Allow access to anyone (no login required)

    def get(self, request):
        available_books = Book.objects.filter(copies_available__gt=0)  # Filter only available books
        serializer = BookSerializer(available_books, many=True)
        return Response(serializer.data)


class LibraryUserViewSet(viewsets.ModelViewSet):
    queryset = LibraryUser.objects.all()
    serializer_class = LibraryUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class TransactionViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def checkout(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        user = request.user.libraryuser

        if book.copies_available > 0:
            book.copies_available -= 1
            book.save()
            transaction = Transaction.objects.create(user=user, book=book)
            return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)
        return Response({'error': 'No copies available'}, status=status.HTTP_400_BAD_REQUEST)

    def return_book(self, request, pk=None):
        transaction = get_object_or_404(Transaction, pk=pk)
        book = transaction.book

        transaction.return_date = timezone.now()
        transaction.save()
        book.copies_available += 1
        book.save()
        return Response({'message': 'Book returned successfully'}, status=status.HTTP_200_OK)

    def list_checkout_history(self, request):
        user = request.user.libraryuser
        transactions = Transaction.objects.filter(user=user)
        return Response(TransactionSerializer(transactions, many=True).data)
