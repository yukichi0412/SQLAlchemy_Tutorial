from django.shortcuts import render

import django_filters
from rest_framework import viewsets, filters

from .models import Category
from .serializer import CategorySerializer

from config.db import make_session

class CategoryViewSet(viewsets.ModelViewSet):
    Session = make_session()
    queryset = Session.query(Category).all()
    serializer_class = CategorySerializer
