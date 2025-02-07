from django import forms

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

    class Meta:
        model = Match
        fields = "__all__"
