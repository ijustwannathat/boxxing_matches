from rest_framework import generics

from .models import Boxer, Match, MatchResult
from .serializers import BoxerSerializer, MatchResultSerializer, MatchSerializer


class BoxerView(generics.ListCreateAPIView):
    queryset = Boxer.objects.all()
    serializer_class = BoxerSerializer
    name = "boxer"


class BoxerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Boxer.objects.all()
    serializer_class = BoxerSerializer
    name = "boxer-detail"


class MatchView(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    name = "match"


class MatchDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    name = "match-detail"


class MatchResultView(generics.ListCreateAPIView):
    queryset = MatchResult.objects.all()
    serializer_class = MatchResultSerializer
    name = "match-result"


class MatchResultDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MatchResult.objects.all()
    serializer_class = MatchResultSerializer
    name = "match-result-detail"
