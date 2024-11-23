from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UpdateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['available']

    def validate_available(self, value):
        if not isinstance(value, bool):  # Exemplo: exige um valor booleano
            raise serializers.ValidationError("The 'available' field must be a boolean.")
        return value