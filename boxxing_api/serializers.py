from rest_framework import serializers

from .models import Boxer, BoxerPerformance, Match, MatchResult


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


class MatchSerializer(serializers.ModelSerializer):
    match_result_url = serializers.HyperlinkedRelatedField(
        view_name="matchresult-detail",
        read_only=True,
        lookup_field="pk",
        source="matchresult",
    )

    class Meta:
        model = Match
        fields = (
            "id",
            "location",
            "total_rounds",
            "date",
            "boxer_1",
            "boxer_2",
            "winner",
            "match_result_url",
        )


class MatchResultSerializer(serializers.HyperlinkedModelSerializer):
    match = MatchSerializer(read_only=True)

    class Meta:
        model = MatchResult
        fields = "__all__"


class BoxerPerformanceSerializer(serializers.ModelSerializer):
    match_result = MatchResultSerializer(many=True)

    class Meta:
        model = BoxerPerformance
        fields = "__all__"

    def get_boxer_performances(self, match):
        perormances = BoxerPerformance.objects.filter(match_result__match=match)
        return BoxerPerformance(perormances, many=True).data
