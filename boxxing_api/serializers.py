from rest_framework import serializers

from .models import Boxer, BoxerMatch, Match, Rounds
from .weight_category import define_weight_category


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


class RoundsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rounds
        fields = "__all__"


class BoxerMatchSerializer(serializers.ModelSerializer):
    total_rounds = RoundsSerializer(many=False, read_only=False)

    class Meta:
        model = BoxerMatch
        fields = ("total_rounds", "boxer")


class MatchSerializer(serializers.ModelSerializer):
    boxer_1 = BoxerMatchSerializer(many=False, read_only=True)
    boxer_2 = BoxerMatchSerializer(many=False, read_only=True)

    class Meta:
        model = Match
        fields = ("boxer_1", "boxer_2")
