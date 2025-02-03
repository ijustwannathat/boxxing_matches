from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register("boxers", views.BoxerViewSet)
router.register("matches", views.MatchViewSet)
router.register("match-results", views.MatchResultViewSet)


urlpatterns = [path("", include(router.urls))]
