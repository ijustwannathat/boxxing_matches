from django.db import models
from django_countries.fields import CountryField

from .weight_category import define_weight_category


class Boxer(models.Model):
    name = models.CharField(max_length=120)
    second_name = models.CharField(max_length=120)
    height = models.PositiveSmallIntegerField()
    age = models.PositiveSmallIntegerField()
    weight = models.FloatField()
    country = CountryField()
    fights_won = models.PositiveSmallIntegerField(default=0)
    fights_lost = models.PositiveSmallIntegerField(default=0)
    fights_tied = models.PositiveSmallIntegerField(default=0)
    fights_played = models.PositiveSmallIntegerField(default=0)
    weight_category = models.CharField(max_length=120, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.weight_category = define_weight_category(self.weight)
        super(Boxer, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.weight_category}"


class Match(models.Model):
    boxer_1 = models.ForeignKey(
        Boxer,
        on_delete=models.CASCADE,
        related_name="match_boxer_1",
    )
    boxer_2 = models.ForeignKey(
        Boxer,
        on_delete=models.CASCADE,
        related_name="match_boxer_2",
    )
    location = models.CharField(max_length=255, blank=True, null=True)
    total_rounds = models.PositiveSmallIntegerField(default=4)
    winner = models.ForeignKey(
        Boxer, on_delete=models.SET_NULL, blank=True, null=True, related_name="wins"
    )
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Match: {self.boxer_1.name} vs {self.boxer_2.name} - {self.date.strftime('%Y:%m:%d')}"


class MatchResult(models.Model):
    match = models.OneToOneField(Match, on_delete=models.CASCADE)
    boxer = models.ForeignKey(
        Boxer, on_delete=models.CASCADE, related_name="match_results"
    )
    winner = models.ForeignKey(
        Boxer,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="match_victories",
    )
    knockout_round = models.PositiveSmallIntegerField(default=0)
    first_boxer_score = models.PositiveSmallIntegerField()
    second_boxer_score = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Match {self.match} ends with winner: \n Boxer {self.boxer.name} {self.boxer.second_name}"


class BoxerPerformance(models.Model):
    match_result = models.ForeignKey(MatchResult, on_delete=models.CASCADE)
    boxer = models.ForeignKey(Boxer, on_delete=models.CASCADE)
    total_punces = models.PositiveSmallIntegerField()
    punch_accuracy = models.DecimalField(max_digits=5, decimal_places=2)
    knockdowns = models.PositiveSmallIntegerField()
    rounds_won = models.PositiveSmallIntegerField()
    total_defense = models.PositiveSmallIntegerField()

    # def save(self, *args, **kwargs):
    #     self.punch_accuracy = ...
    def __str__(self):
        return f"{self.boxer.name.capitalize()} performance in a match"
