from rest_framework import viewsets

from .models import Boxer, BoxerPerformance, Match, MatchResult
from .serializers import (
    BoxerPerformanceSerializer,
    BoxerSerializer,
    MatchResultSerializer,
    MatchSerializer,
)


class BoxerViewSet(viewsets.ModelViewSet):
    queryset = Boxer.objects.all()
    serializer_class = BoxerSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchResultViewSet(viewsets.ModelViewSet):
    queryset = MatchResult.objects.all()
    serializer_class = MatchResultSerializer
