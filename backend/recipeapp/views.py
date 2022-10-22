from django.shortcuts import render
from rest_framework import viewsets
from .models import RecipeModel
from .serializers import RecipeSerializer
# Create your views here.

class RecipeView(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = RecipeModel.objects.all()
