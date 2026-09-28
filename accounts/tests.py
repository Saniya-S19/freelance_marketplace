from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_find_freelancers_link_redirects_to_freelancers_page(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, reverse('find_freelancers'))
