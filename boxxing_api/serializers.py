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

    rounds = RoundSerializer(many=True, read_only=True)

    class Meta:
        model = Match
        fields = [
            "boxer_1",
            "boxer_2",
            "location",
            "total_rounds",
            "winner",
            "date",
            "rounds",
        ]


class MatchResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = MatchResult
        fields = "__all__"
