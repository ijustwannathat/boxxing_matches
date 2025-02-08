from django import forms
from django.core.exceptions import ValidationError

from boxxing_api.models import Boxer, Match


class MatchForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields["winner"].queryset = Boxer.objects.filter(
                pk__in=[self.instance.boxer_1.pk, self.instance.boxer_2.pk]
            )
        else:
            self.fields["winner"].queryset = Boxer.objects.none()

    def clean(self):
        cleaned_data = super().clean()
        boxer_1 = cleaned_data.get("boxer_1")
        boxer_2 = cleaned_data.get("boxer_2")
        total_rounds = cleaned_data.get("total_rounds")
        if boxer_1.pk == boxer_2.pk:
            raise ValidationError("boxer_1 and boxer_2 should not be the same person")
        if total_rounds > 12:
            raise ValidationError(
                f"Maximum amount of rounds is limited to 12, you inserted {total_rounds} instead"
            )

    class Meta:
        model = Match
        fields = "__all__"


class BoxerForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        boxer_age = cleaned_data.get("age")
        boxer_weight = cleaned_data.get("weight")
        boxer_height = cleaned_data.get("height")

        if not all((boxer_height < 350, boxer_age < 122, boxer_weight < 300)):
            raise ValidationError("Either age, weight or height is beyond restriction")
