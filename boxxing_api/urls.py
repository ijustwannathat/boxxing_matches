from django.urls import path

from . import views

urlpatterns = [
    path("boxers/", views.BoxerView.as_view()),
    path("boxers/<int:pk>/", views.BoxerDetailView.as_view()),
    path("matches/", views.MatchView.as_view()),
    path("matches/<int:pk>/", views.MatchDetailView.as_view()),
]
