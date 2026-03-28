from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import Author, Book, Loan
from .serializers import AuthorSerializer, BookListSerializer, LoanSerializer, BookCreateUpdateSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    
class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["action", "update", "partial_update"]:
            return BookCreateUpdateSerializer
        return BookListSerializer

    @action(detail=True, methods=["get"])
    def loans(self, request, pk=None):
        # detail=True car on accède à un objet spécifique
        # methods pour les méthodes autorisées
        """
        Récupérer tous les emprunts associés à un livre spécifique.
        """
        book = self.get_object()
        loans = Loan.objects.filter(book=book)
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)