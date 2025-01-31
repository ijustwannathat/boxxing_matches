# Generated by Django 5.1.4 on 2025-01-31 17:42

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
                    models.CharField(
                        blank=True,
                        default="Lightweight",
                        editable=False,
                        max_length=120,
                    ),
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
                (
                    "winner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="wins",
                        to="boxxing_api.boxer",
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
                ("total_rounds", models.PositiveSmallIntegerField(default=0)),
                (
                    "win_method",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("KO", "Knockout"),
                            ("TKO", "Technical Knockout"),
                            ("UD", "Unanonimous Decision"),
                            ("SD", "Split Decision"),
                            ("MD", "Majority Decision"),
                            ("Draw", "Draw"),
                            ("NC", "No Contest"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="boxxing_api.match",
                    ),
                ),
                (
                    "winner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="boxxing_api.boxer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Round",
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
                ("round_number", models.PositiveSmallIntegerField(default=4)),
                ("first_boxer_score", models.PositiveSmallIntegerField(default=0)),
                ("second_boxer_score", models.PositiveSmallIntegerField(default=0)),
                (
                    "match",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="round_number",
                        to="boxxing_api.match",
                    ),
                ),
                (
                    "winner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="winner",
                        to="boxxing_api.boxer",
                    ),
                ),
            ],
            options={
                "unique_together": {("match", "round_number")},
            },
        ),
    ]
