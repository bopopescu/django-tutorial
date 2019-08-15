from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer
from .models import Language, Programmer, Paradigm

# Create your views here.
class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer


class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer