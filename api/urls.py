from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.views import AuthorViewSet, BookViewSet, LoanViewSet 

router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'loans', LoanViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
