# Generated by Django 5.1.4 on 2025-02-06 20:20

import django.db.models.deletion
import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Boxer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120)),
                ("second_name", models.CharField(max_length=120)),
                ("height", models.PositiveSmallIntegerField()),
                ("age", models.PositiveSmallIntegerField()),
                ("weight", models.FloatField()),
                ("country", django_countries.fields.CountryField(max_length=2)),
                ("fights_won", models.PositiveSmallIntegerField(default=0)),
                ("fights_lost", models.PositiveSmallIntegerField(default=0)),
                ("fights_tied", models.PositiveSmallIntegerField(default=0)),
                ("fights_played", models.PositiveSmallIntegerField(default=0)),
                (
                    "weight_category",
                    models.CharField(blank=True, editable=False, max_length=120),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Match",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                ("total_rounds", models.PositiveSmallIntegerField(default=4)),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "boxer_1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="match_boxer_1",
                        to="boxxing_api.boxer",
                    ),
                ),
                (
                    "boxer_2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="match_boxer_2",
                        to="boxxing_api.boxer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BoxerPerformance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "boxer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="performances",
                        to="boxxing_api.boxer",
                    ),
                ),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="performances",
                        to="boxxing_api.match",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MatchResult",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total_punces", models.PositiveSmallIntegerField()),
                ("punch_accuracy", models.DecimalField(decimal_places=2, max_digits=5)),
                ("knockdowns", models.PositiveSmallIntegerField()),
                ("rounds_won", models.PositiveSmallIntegerField()),
                ("total_defense", models.PositiveSmallIntegerField()),
                (
                    "boxer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="boxxing_api.boxer",
                    ),
                ),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="match_results",
                        to="boxxing_api.match",
                    ),
                ),
            ],
        ),
    ]
