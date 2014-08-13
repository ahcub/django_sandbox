from django.test import TestCase


class TestMain(TestCase):
    def test_index(self):
        response = self.client.get('')
        print(response._container)
        self.assertContains(response, 'tutorial_app')
        self.assertContains(response, 'models_')