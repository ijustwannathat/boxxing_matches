from rest_framework import serializers

from .models import Boxer, Match, MatchResult, Round


class BoxerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Boxer
        fields = (
            "name",
            "second_name",
            "age",
            "weight",
            "height",
            "fights_won",
            "fights_lost",
            "weight_category",
        )
        read_only_fields = ("weight_category",)


class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = "__all__"


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = "__all__"


class MatchResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = MatchResult
        fields = "__all__"
