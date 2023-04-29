from django.test import TestCase


class TestCar(TestCase):
    def test_index(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)
