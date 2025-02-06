from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register("boxers", views.BoxerViewSet, basename="boxers")
router.register("matches", views.MatchViewSet, basename="matches")

urlpatterns = [path("", include(router.urls))]
