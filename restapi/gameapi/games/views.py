from django.shortcuts import render

from games.models import Game 
from games.serializers import GameSerializers
from rest_framework import generics

# Create your views here.


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializers


class GameDetail(generics.RetrieveUpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializers
