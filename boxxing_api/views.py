from rest_framework import generics

from .models import Boxer, BoxerMatch, Match
from .serializers import BoxerMatchSerializer, BoxerSerializer, MatchSerializer

print('hello', "data")
class BoxerView(generics.ListCreateAPIView):
    queryset = Boxer.objects.all()
    serializer_class = BoxerSerializer
    name = "boxer"


class BoxerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Boxer.objects.all()
    serializer_class = BoxerSerializer
    name = "boxer-detail"


class BoxerMatchView(generics.ListCreateAPIView):
    queryset = BoxerMatch.objects.all()
    serializer_class = BoxerMatchSerializer
    name = "boxer-match"


class BoxerMatchDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoxerMatch.objects.all()
    serializer_class = BoxerMatchSerializer
    name = "boxer-match-detail"


class MatchView(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    name = "match"


class MatchDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    name = "match-detail"



class MatchView(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    name = "match"
