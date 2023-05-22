from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Provider
from .serializers import ProviderSerializer

# Create your views here.


class ProviderViewSet(ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
