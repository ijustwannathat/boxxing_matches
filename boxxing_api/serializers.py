from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Boxer, Match, MatchResult


class BoxerSerializer(serializers.ModelSerializer):
    def validate_age(self, age):
        if age > 122:
            raise serializers.ValidationError("Age is restricted to 122")
        return age

    def validate_height(self, height):
        if height > 350:
            raise serializers.ValidationError("Height can not be over 350")
        return height

    def validate_weight(self, weight):
        if weight > 300:
            raise serializers.ValidationError("Weight can not be over 350")
        return weight

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
            "fights_played",
        )
        read_only_fields = ("weight_category", "fights_played")


class BoxerResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boxer
        fields = ("id", "name", "second_name")


class MatchResultSerializer(serializers.ModelSerializer):
    boxer = BoxerResultSerializer()

    def validate(self, validated_data):
        match_id = validated_data.get("match")
        rounds_won = validated_data.get("rounds_won")
        match = get_object_or_404(Match, pk=match_id)
        boxer_1 = get_object_or_404(
            MatchResult, match=match.match_id, boxer=Boxer.match.boxer_1.pk
        )
        boxer_2 = get_object_or_404(
            MatchResult, match=match.match_id, boxer=Boxer.match.boxer_2.pk
        )
        total_rounds = match.total_rounds

        if rounds_won > total_rounds:
            raise serializers.ValidationError(
                "The amount of won rounds cannot exceed total rounds"
            )
        if (
            boxer_1.total_defense > boxer_2.total_punches
            or boxer_2.total_defense > boxer_1.total_punches
        ):
            raise serializers.ValidationError(
                "It is impossible to defend more time than the punches thrown"
            )

        return validated_data

    class Meta:
        model = MatchResult
        fields = "__all__"


class MatchSerializer(serializers.ModelSerializer):
    boxer_1 = BoxerSerializer(read_only=True)
    boxer_2 = BoxerSerializer(read_only=True)
    match_results = MatchResultSerializer(many=True, read_only=True)

    winner = BoxerResultSerializer(read_only=True)

    def validate(self, validated_data):
        boxer_1 = validated_data.get("boxer_1")
        boxer_2 = validated_data.get("boxer_2")
        winner = validated_data.get("winner")
        if boxer_1.pk == boxer_2.pk:
            raise serializers.ValidationError(
                "boxer_1 and boxer_2 cannot be the same person \n boxers cannot fight themselves"
            )
        if winner.pk is None:
            pass

        if isinstance(winner.pk, int) and winner.pk not in (
            boxer_1.pk,
            boxer_2.pk,
        ):
            raise serializers.ValidationError(
                "Winner should be the one who contested in the match"
            )

        return validated_data

    def validate_total_rounds(self, total_rounds):
        if total_rounds > 12:
            raise serializers.ValidationError("Amount of rounds is restricted to 12")
        return total_rounds

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
