from django.contrib import admin
from django.urls import path, include
from app.views import author_list_and_create, author_detail, loan_list, book_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', author_list_and_create, name='author-list-create'),
    path('author/<int:pk>/', author_detail, name='author-detail'),
    path('loans/', loan_list, name='loan-list'),
    path('books/', book_list, name='book-list'),
]
