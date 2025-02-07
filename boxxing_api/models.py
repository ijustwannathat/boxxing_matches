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
    fights_played = models.PositiveSmallIntegerField(default=0, editable=False)
    weight_category = models.CharField(max_length=120, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.weight_category = define_weight_category(self.weight)
        self.fights_played = self.fights_won + self.fights_lost + self.fights_tied
        super(Boxer, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.second_name}"


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

    win_choices = (
        ("KO", "Knockout"),
        ("TKO", "Technical Knockout"),
        ("UD", "Unanonimous Decision"),
        ("SD", "Split Decision"),
        ("MD", "Majority Decision"),
        ("Draw", "Draw"),
        ("NC", "No Contest"),
    )
    win_method = models.CharField(max_length=50, choices=win_choices, blank=True)

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Match: {self.boxer_1.name} vs {self.boxer_2.name} - {self.date.strftime('%Y:%m:%d')}"


class MatchResult(models.Model):
    match = models.ForeignKey(
        Match, on_delete=models.CASCADE, related_name="match_results"
    )
    boxer = models.ForeignKey(Boxer, on_delete=models.CASCADE)
    total_punces = models.PositiveSmallIntegerField(default=0)
    punch_accuracy = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    knockdowns = models.PositiveSmallIntegerField(default=0)
    rounds_won = models.PositiveSmallIntegerField(default=0)
    total_defense = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"Match result for {self.boxer} in weight cateogry {self.boxer.weight_category}"
