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
    weight_category = models.CharField(
        max_length=120, default="Lightweight", blank=True, editable=False
    )

    def save(self, *args, **kwargs):
        self.weight_category = define_weight_category(self.weight)
        super(Boxer, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Rounds(models.Model):
    round = models.PositiveSmallIntegerField(default=0)


class BoxerMatch(models.Model):
    boxer = models.ForeignKey(
        Boxer,
        related_name="contestant",
        on_delete=models.CASCADE,
    )
    total_rounds = models.ForeignKey(
        Rounds, related_name="total_rounds", on_delete=models.CASCADE
    )


class Match(models.Model):
    boxer_1 = models.ForeignKey(
        BoxerMatch, related_name="first_contestant", on_delete=models.CASCADE
    )
    boxer_2 = models.ForeignKey(
        BoxerMatch, related_name="second_contestant", on_delete=models.CASCADE
    )
