from rest_framework import serializers

from .models import Boxer, Match, MatchResult


class BoxerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Boxer
        fields = (
            "id",
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


class BoxerResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boxer
        fields = ("id", "name", "second_name")


class MatchResultSerializer(serializers.ModelSerializer):
    boxer = BoxerResultSerializer()

    class Meta:
        model = MatchResult
        fields = "__all__"


class MatchSerializer(serializers.ModelSerializer):
    boxer_1 = BoxerSerializer()
    boxer_2 = BoxerSerializer()
    match_results = MatchResultSerializer(many=True, read_only=True)

    class Meta:
        model = Match
        fields = [
            "id",
            "boxer_1",
            "boxer_2",
            "location",
            "total_rounds",
            "date",
            "match_results",
            "winner",
            "win_method",
        ]
