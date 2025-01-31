from django.contrib import admin

from .models import Boxer, Match, MatchResult

admin.site.register(Boxer)
admin.site.register(Match)
admin.site.register(MatchResult)
