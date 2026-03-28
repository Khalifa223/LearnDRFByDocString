from rest_framework import serializers
from .models import Author, Book, Loan

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
    
    def validate_name(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("Le nom doit commencer par une majuscule.")
        return value
    
class BookCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']
class BookListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    is_borrowed_by_me = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = '__all__'
    
    def get_is_borrowed_by_me(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return Loan.objects.filter(book=obj, user=request.user, return_date__isnull=True).exists()
        return False

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'
        
    def validate(self, data):
        if self.instance is None and data.get("return_date"):
            raise serializers.ValidationError("Impossible de créer un emprunt déjà retourné.")
        
        if self.instance is None:
            if existing_loan := Loan.objects.filter(book=data.get("book"), return_date__isnull=True):
                raise serializers.ValidationError("Ce livre est déjà emprunté.")
            
        if self.instance and data.get('return_date') and data['return_date'] < self.instance.borrow_date:
                raise serializers.ValidationError("La date de retour doit être après la date d'emprunt.")
        
        return data