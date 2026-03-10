from django.contrib import admin
from django.urls import path, include
from app.views import author_list_and_create


urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', author_list_and_create, name='author-list-create'),
]
