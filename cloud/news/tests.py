from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import datetime

from .models import News

User = get_user_model()

class NewsTestCases(TestCase):
    @classmethod
    def setUpTestData(cls):
        news = News.objects.create(
            title="новость",
            anons="анонс",
            full_text="wwwww",
            date=datetime(2025, 4, 4, 7, 41, 0, 806429),
        )

    def setUp(self) -> None:
        self.user = User.objects.create(
            username="testuser",
            password="password",
        )

    def test_valid_date_to_news(self):
        news = News.objects.get(id=1)
        self.assertTrue(datetime.now() <= news.date)

    def test_max_length(self):
        news = News.objects.get(id=1)

        title_max_length = news._meta.get_field('title').max_length
        anons_max_length = news._meta.get_field('anons').max_length
        slug_max_length = news._meta.get_field('slug').max_length

        self.assertEquals(title_max_length, 50)
        self.assertEquals(anons_max_length, 250)
        self.assertEquals(slug_max_length, 16)

    def test_valid_value_in_news(self):
        news = News.objects.get(id=1)

        title = news.title
        anons = news.anons
        slug = news.slug
        full_text = news.full_text

        self.assertEquals(title, 'новость')
        self.assertEquals(anons, 'анонс')
        self.assertTrue(len(slug) != 0)
        self.assertTrue(full_text == 'wwwww')