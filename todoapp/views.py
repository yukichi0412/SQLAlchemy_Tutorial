from django.shortcuts import render

import django_filters
from rest_framework import viewsets, filters

from .models import Category
from .serializer import CategorySerializer

from config.settings import Session

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Session.query(Category).all()
    serializer_class = CategorySerializer
