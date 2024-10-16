from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, LibraryUserViewSet, TransactionViewSet, BookListView
from .views import custom_login_view

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'users', LibraryUserViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Routes for CRUD operations on books and users
    path('login/', custom_login_view, name='login'),
    path('api-auth/', include('rest_framework.urls')),
    path('available-books/', BookListView.as_view(), name='available_books'),  # Public booklist (available books)
    path('transactions/checkout/<int:pk>/', TransactionViewSet.as_view({'post': 'checkout'}), name='checkout'),
    path('transactions/return/<int:pk>/', TransactionViewSet.as_view({'post': 'return_book'}), name='return_book'),
    path('transactions/history/', TransactionViewSet.as_view({'get': 'list_checkout_history'}), name='checkout_history'),
]
