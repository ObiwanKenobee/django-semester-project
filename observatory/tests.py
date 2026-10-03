from django.test import TestCase
from django.urls import reverse
from .models import IntelligenceSignal


class IntelligenceSignalModelTests(TestCase):
    def test_model_creation(self):
        signal = IntelligenceSignal.objects.create(
            title='Test Signal',
            category=IntelligenceSignal.Category.WATER,
            status=IntelligenceSignal.Status.OBSERVED,
        )
        self.assertEqual(str(signal), 'Test Signal')
        self.assertEqual(signal.status, 'Observed')


class HomePageTests(TestCase):
    def test_home_returns_200(self):
        response = self.client.get(reverse('observatory:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_contains_brand(self):
        response = self.client.get(reverse('observatory:home'))
        self.assertContains(response, 'Atlas Sanctum Observatory')


class SignalsPageTests(TestCase):
    def setUp(self):
        IntelligenceSignal.objects.create(
            title='Water Test Signal',
            category=IntelligenceSignal.Category.WATER,
            status=IntelligenceSignal.Status.OBSERVED,
        )

    def test_signals_returns_200(self):
        response = self.client.get(reverse('observatory:signals'))
        self.assertEqual(response.status_code, 200)

    def test_signals_lists_records(self):
        response = self.client.get(reverse('observatory:signals'))
        self.assertContains(response, 'Water Test Signal')


class SignalDetailTests(TestCase):
    def setUp(self):
        self.signal = IntelligenceSignal.objects.create(
            title='Detail Test Signal',
            category=IntelligenceSignal.Category.ECOLOGY,
            status=IntelligenceSignal.Status.VERIFIED,
            location='Nairobi, Kenya',
        )

    def test_detail_returns_200(self):
        response = self.client.get(reverse('observatory:signal_detail', args=[self.signal.pk]))
        self.assertEqual(response.status_code, 200)

    def test_detail_contains_title(self):
        response = self.client.get(reverse('observatory:signal_detail', args=[self.signal.pk]))
        self.assertContains(response, 'Detail Test Signal')

    def test_invalid_signal_returns_404(self):
        response = self.client.get(reverse('observatory:signal_detail', args=[99999]))
        self.assertEqual(response.status_code, 404)


class AboutPageTests(TestCase):
    def test_about_returns_200(self):
        response = self.client.get(reverse('observatory:about'))
        self.assertEqual(response.status_code, 200)

    def test_about_contains_content(self):
        response = self.client.get(reverse('observatory:about'))
        self.assertContains(response, 'Atlas Sanctum')
