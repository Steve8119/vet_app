from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Animal
from rest_framework import generics
from .forms import AnimalForm
from .serializers import AnimalSerializer, SignUpSerializer
from django.contrib.auth.models import User


# Remove template-based home view, as it’s now API-driven
@api_view(['GET'])
def home(request):
    return Response({"message": "Welcome to the Animal Management API."})


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def animal_management(request, animal_id=None):
    if request.method == 'GET':
        if animal_id:
            try:
                animal = Animal.objects.get(pk=animal_id, user=request.user)
                serializer = AnimalSerializer(animal)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Animal.DoesNotExist:
                return Response({"error": "Animal not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            animals = Animal.objects.filter(user=request.user)
            serializer = AnimalSerializer(animals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            animal = serializer.save(user=request.user)
            return Response(AnimalSerializer(animal).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        if not animal_id:
            return Response({"error": "Animal ID is required for updating."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            animal = Animal.objects.get(pk=animal_id, user=request.user)
        except Animal.DoesNotExist:
            return Response({"error": "Animal not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AnimalSerializer(animal, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        if not animal_id:
            return Response({"error": "Animal ID is required for deletion."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            animal = Animal.objects.get(pk=animal_id, user=request.user)
            animal.delete()
            return Response({"message": "Animal deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Animal.DoesNotExist:
            return Response({"error": "Animal not found."}, status=status.HTTP_404_NOT_FOUND)

# User login API
@api_view(['POST'])
def viewlog(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)

    if user is not None:
        login(request, user)
        return Response({"message": "Successfully logged in!"}, status=status.HTTP_200_OK)
    return Response({"error": "Invalid email or password."}, status=status.HTTP_400_BAD_REQUEST)


# User signup API
@api_view(['POST'])
def viewsign(request):
    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()
        login(request, user)
        return Response({"message": "Account created and logged in successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


