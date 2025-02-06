from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Boxer, Match, MatchResult


class MatchResultAdmin(admin.TabularInline):
    model = MatchResult
    extra = 2


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    inline = [MatchResultAdmin]


@admin.register(Boxer)
class BoxerAdmin(admin.ModelAdmin):
    list_display = ["name", "second_name", "fights_won", "fights_played"]


@admin.register(MatchResult)
class MatchResultAdmin(admin.ModelAdmin):
    list_display = [
        "match",
        "boxer",
        "total_punces",
        "punch_accuracy",
        "knockdowns",
        "rounds_won",
        "total_defense",
    ]


@receiver(post_save, sender=Match)
def create_match_results(sender, instance, created, **kwargs):
    if created:
        MatchResult.objects.get_or_create(match=instance, boxer=instance.boxer_1)
        MatchResult.objects.get_or_create(match=instance, boxer=instance.boxer_2)
