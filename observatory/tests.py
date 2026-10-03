from django.test import TestCase
from django.urls import reverse
from .models import (
    IntelligenceSignal, Evidence, Assessment,
    Opportunity, ActionItem, ImpactRecord, Organisation,
)


# ── Helpers ───────────────────────────────────────────────────────────────────

def make_signal(**kwargs):
    defaults = {
        'title': 'Test Signal',
        'category': IntelligenceSignal.Category.WATER,
        'status': IntelligenceSignal.Status.OBSERVED,
    }
    defaults.update(kwargs)
    return IntelligenceSignal.objects.create(**defaults)


def make_opportunity(signal, **kwargs):
    defaults = {'title': 'Test Opportunity', 'status': Opportunity.OpportunityStatus.IDENTIFIED}
    defaults.update(kwargs)
    return Opportunity.objects.create(signal=signal, **defaults)


def make_action(opportunity, **kwargs):
    defaults = {'title': 'Test Action', 'status': ActionItem.ActionStatus.PROPOSED}
    defaults.update(kwargs)
    return ActionItem.objects.create(opportunity=opportunity, **defaults)


# ── Phase 1 — Core ────────────────────────────────────────────────────────────

class IntelligenceSignalModelTests(TestCase):
    def test_model_creation(self):
        signal = make_signal()
        self.assertEqual(str(signal), 'Test Signal')
        self.assertEqual(signal.status, 'Observed')

    def test_has_coordinates_false_without_coords(self):
        self.assertFalse(make_signal().has_coordinates)

    def test_has_coordinates_true_with_coords(self):
        signal = make_signal(latitude=-1.286389, longitude=36.817223)
        self.assertTrue(signal.has_coordinates)


class HomePageTests(TestCase):
    def test_home_returns_200(self):
        self.assertEqual(self.client.get(reverse('observatory:home')).status_code, 200)

    def test_home_contains_brand(self):
        self.assertContains(self.client.get(reverse('observatory:home')), 'Atlas Sanctum Observatory')


class SignalsPageTests(TestCase):
    def setUp(self):
        make_signal(title='Water Test Signal')

    def test_signals_returns_200(self):
        self.assertEqual(self.client.get(reverse('observatory:signals')).status_code, 200)

    def test_signals_lists_records(self):
        self.assertContains(self.client.get(reverse('observatory:signals')), 'Water Test Signal')

    def test_signals_filter_by_category(self):
        make_signal(title='Ecology Signal', category=IntelligenceSignal.Category.ECOLOGY)
        response = self.client.get(reverse('observatory:signals') + '?category=Ecology')
        self.assertContains(response, 'Ecology Signal')
        self.assertNotContains(response, 'Water Test Signal')

    def test_signals_filter_by_status(self):
        make_signal(title='Verified Signal', status=IntelligenceSignal.Status.VERIFIED)
        response = self.client.get(reverse('observatory:signals') + '?status=Verified')
        self.assertContains(response, 'Verified Signal')
        self.assertNotContains(response, 'Water Test Signal')


class SignalDetailTests(TestCase):
    def setUp(self):
        self.signal = make_signal(title='Detail Test Signal', location='Nairobi, Kenya')

    def test_detail_returns_200(self):
        self.assertEqual(self.client.get(reverse('observatory:signal_detail', args=[self.signal.pk])).status_code, 200)

    def test_detail_contains_title(self):
        self.assertContains(self.client.get(reverse('observatory:signal_detail', args=[self.signal.pk])), 'Detail Test Signal')

    def test_invalid_signal_returns_404(self):
        self.assertEqual(self.client.get(reverse('observatory:signal_detail', args=[99999])).status_code, 404)


class AboutPageTests(TestCase):
    def test_about_returns_200(self):
        self.assertEqual(self.client.get(reverse('observatory:about')).status_code, 200)

    def test_about_contains_content(self):
        self.assertContains(self.client.get(reverse('observatory:about')), 'Atlas Sanctum')


# ── Phase 2 — Evidence ────────────────────────────────────────────────────────

class EvidenceModelTests(TestCase):
    def test_evidence_creation(self):
        signal = make_signal()
        ev = Evidence.objects.create(
            signal=signal, title='Test Evidence',
            evidence_type=Evidence.EvidenceType.OBSERVATION,
            reliability=Evidence.Reliability.PLAUSIBLE,
        )
        self.assertIn(signal.title, str(ev))


class EvidenceViewTests(TestCase):
    def setUp(self):
        self.signal = make_signal()
        self.ev = Evidence.objects.create(
            signal=self.signal, title='Test Evidence',
            evidence_type=Evidence.EvidenceType.REPORT,
            reliability=Evidence.Reliability.CONFIRMED,
        )

    def test_evidence_list_returns_200(self):
        self.assertEqual(self.client.get(reverse('observatory:evidence_list', args=[self.signal.pk])).status_code, 200)

    def test_evidence_list_contains_item(self):
        self.assertContains(self.client.get(reverse('observatory:evidence_list', args=[self.signal.pk])), 'Test Evidence')

    def test_evidence_detail_returns_200(self):
        self.assertEqual(self.client.get(reverse('observatory:evidence_detail', args=[self.signal.pk, self.ev.pk])).status_code, 200)

    def test_evidence_detail_wrong_signal_returns_404(self):
        other = make_signal(title='Other')
        self.assertEqual(self.client.get(reverse('observatory:evidence_detail', args=[other.pk, self.ev.pk])).status_code, 404)


# ── Phase 3 — Geospatial ──────────────────────────────────────────────────────

class MapViewTests(TestCase):
    def test_map_returns_200(self):
        self.assertEqual(self.client.get(reverse('observatory:signal_map')).status_code, 200)

    def test_map_shows_mapped_signals(self):
        make_signal(title='Mapped Signal', latitude=-1.286389, longitude=36.817223)
        self.assertContains(self.client.get(reverse('observatory:signal_map')), 'Mapped Signal')

    def test_map_excludes_unmapped_signals(self):
        make_signal(title='Unmapped Signal')
        self.assertNotContains(self.client.get(reverse('observatory:signal_map')), 'Unmapped Signal')


# ── Phase 4 — Opportunities ───────────────────────────────────────────────────

class OpportunityModelTests(TestCase):
    def test_opportunity_creation(self):
        opp = make_opportunity(make_signal())
        self.assertEqual(str(opp), 'Test Opportunity')


class OpportunityViewTests(TestCase):
    def setUp(self):
        self.signal = make_signal()
        self.opp = make_opportunity(self.signal, title='Water Opportunity')

    def test_opportunity_list_returns_200(self):
        self.assertEqual(self.client.get(reverse('observatory:opportunity_list')).status_code, 200)

    def test_opportunity_list_contains_item(self):
        self.assertContains(self.client.get(reverse('observatory:opportunity_list')), 'Water Opportunity')

    def test_opportunity_detail_returns_200(self):
        self.assertEqual(self.client.get(reverse('observatory:opportunity_detail', args=[self.opp.pk])).status_code, 200)

    def test_opportunity_detail_404(self):
        self.assertEqual(self.client.get(reverse('observatory:opportunity_detail', args=[99999])).status_code, 404)


# ── Phase 5 — Assessment ──────────────────────────────────────────────────────

class AssessmentModelTests(TestCase):
    def test_assessment_creation(self):
        signal = make_signal()
        a = Assessment.objects.create(signal=signal, summary='Test summary', priority=Assessment.Priority.HIGH)
        self.assertIn(signal.title, str(a))


class AssessmentViewTests(TestCase):
    def setUp(self):
        self.signal = make_signal()
        Assessment.objects.create(signal=self.signal, summary='Test summary', priority=Assessment.Priority.MEDIUM)

    def test_assessment_detail_returns_200(self):
        self.assertEqual(self.client.get(reverse('observatory:assessment_detail', args=[self.signal.pk])).status_code, 200)

    def test_assessment_detail_no_assessment_returns_404(self):
        other = make_signal(title='No Assessment Signal')
        self.assertEqual(self.client.get(reverse('observatory:assessment_detail', args=[other.pk])).status_code, 404)


# ── Phase 7 — Actions ─────────────────────────────────────────────────────────

class ActionItemModelTests(TestCase):
    def test_action_creation(self):
        action = make_action(make_opportunity(make_signal()))
        self.assertEqual(str(action), 'Test Action')


class ActionViewTests(TestCase):
    def setUp(self):
        self.action = make_action(make_opportunity(make_signal()), title='Deploy sensors')

    def test_action_list_returns_200(self):
        self.assertEqual(self.client.get(reverse('observatory:action_list')).status_code, 200)

    def test_action_list_contains_item(self):
        self.assertContains(self.client.get(reverse('observatory:action_list')), 'Deploy sensors')

    def test_action_detail_returns_200(self):
        self.assertEqual(self.client.get(reverse('observatory:action_detail', args=[self.action.pk])).status_code, 200)

    def test_action_detail_404(self):
        self.assertEqual(self.client.get(reverse('observatory:action_detail', args=[99999])).status_code, 404)


# ── Phase 8 — Impact ──────────────────────────────────────────────────────────

class ImpactRecordModelTests(TestCase):
    def test_impact_creation(self):
        action = make_action(make_opportunity(make_signal()))
        impact = ImpactRecord.objects.create(
            action=action, title='Test Impact',
            impact_type=ImpactRecord.ImpactType.SOCIAL,
        )
        self.assertIn('Test Impact', str(impact))


class ImpactViewTests(TestCase):
    def setUp(self):
        action = make_action(make_opportunity(make_signal()))
        ImpactRecord.objects.create(action=action, title='Community Impact', impact_type=ImpactRecord.ImpactType.SOCIAL)

    def test_impact_list_returns_200(self):
        self.assertEqual(self.client.get(reverse('observatory:impact_list')).status_code, 200)

    def test_impact_list_contains_item(self):
        self.assertContains(self.client.get(reverse('observatory:impact_list')), 'Community Impact')


# ── Phase 9 — Organisations ───────────────────────────────────────────────────

class OrganisationModelTests(TestCase):
    def test_organisation_creation(self):
        org = Organisation.objects.create(name='Test Org', country='Kenya')
        self.assertEqual(str(org), 'Test Org')


class OrganisationViewTests(TestCase):
    def setUp(self):
        self.org = Organisation.objects.create(name='Test Institute', country='Kenya')

    def test_organisation_list_returns_200(self):
        self.assertEqual(self.client.get(reverse('observatory:organisation_list')).status_code, 200)

    def test_organisation_list_contains_item(self):
        self.assertContains(self.client.get(reverse('observatory:organisation_list')), 'Test Institute')

    def test_organisation_detail_returns_200(self):
        self.assertEqual(self.client.get(reverse('observatory:organisation_detail', args=[self.org.pk])).status_code, 200)

    def test_organisation_detail_404(self):
        self.assertEqual(self.client.get(reverse('observatory:organisation_detail', args=[99999])).status_code, 404)

    def test_organisation_signal_attribution(self):
        make_signal(title='Attributed Signal', organisation=self.org)
        response = self.client.get(reverse('observatory:organisation_detail', args=[self.org.pk]))
        self.assertContains(response, 'Attributed Signal')
