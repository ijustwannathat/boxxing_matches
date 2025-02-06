from rest_framework import viewsets

from .models import Boxer, Match
from .serializers import BoxerSerializer, MatchSerializer


class BoxerViewSet(viewsets.ModelViewSet):
    queryset = Boxer.objects.all()
    serializer_class = BoxerSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
