import json

from django.test import Client, SimpleTestCase, TestCase
from django.urls import resolve, reverse

from boxxing_api.views import BoxerViewSet, MatchViewSet

from .models import Boxer, Match


class TestUrl(SimpleTestCase):
    def test_boxer_list_url_is_resolved(self):
        url = reverse("boxers-list")
        self.assertEqual(resolve(url).func.__name__, BoxerViewSet.__name__)

    def test_match_list_url_is_resolved(self):
        url = reverse("matches-list")
        self.assertEqual(resolve(url).func.__name__, MatchViewSet.__name__)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.boxer_url = reverse("boxers-list")
        self.matches_url = reverse("matches-list")

    def test_boxers_list_GET(self):

        response = self.client.get(self.boxer_url)

        self.assertEquals(response.status_code, 200)

    def test_matches_list_GET(self):
        response = self.client.get(self.matches_url)
        self.assertEquals(response.status_code, 200)

    def test_post_method(self):
        response = self.client.post(
            self.boxer_url,
            {
                "name": "Pitbull",
                "second_name": "Cool",
                "age": 56,
                "weight": 140.0,
                "height": 190,
                "fights_won": 15,
                "fights_lost": 1,
            },
        )
        self.assertEqual(response.status_code, 201)

    def test_failure_post_method(self):
        response = self.client.post(self.boxer_url)

        self.assertEqual(response.status_code, 400)
