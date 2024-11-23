from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Book
from .serializers import BookSerializer

import json

@api_view(['GET'])
def get_book(request):

    if request.method == 'GET':
        print('entrou no get')
        books = Book.objects.all()                              # Get all objects in books db (return queryset)

        serializer = BookSerializer(books, many=True)
        print(serializer)           # Serialize the object into json 
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_book(request):
    if request.method == 'POST':
        # Passa os dados do corpo da requisição para o serializer
        serializer = BookSerializer(data=request.data)

        # Verifica se os dados são válidos
        if serializer.is_valid():
            serializer.save()  # Salva o novo livro no banco de dados
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Retorna os dados do livro criado

        # Caso os dados sejam inválidos, retorna um erro 400 com os detalhes
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def edit_book(request, book_id):

    try:
        # Tenta obter o livro pelo ID fornecido
        book = Book.objects.get(id=book_id)       
    except:
        return Response({'error:': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
