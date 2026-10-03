from django.core.management.base import BaseCommand
from observatory.models import (
    IntelligenceSignal, Evidence, Assessment,
    Opportunity, ActionItem, ImpactRecord, Organisation,
)

DEMO_NOTE = 'Demo / Simulated'


class Command(BaseCommand):
    help = 'Seed the database with demonstration data for all roadmap phases (clearly labelled).'

    def handle(self, *args, **options):
        # ── Phase 9 — Organisations ───────────────────────────────────────────
        org_sanctum, _ = Organisation.objects.get_or_create(
            name='Atlas Sanctum Research (Demo)',
            defaults={
                'country': 'Kenya',
                'website': 'https://example.com',
                'description': 'Demonstration organisation. Not a real institution.',
            },
        )
        org_water, _ = Organisation.objects.get_or_create(
            name='East Africa Water Institute (Demo)',
            defaults={
                'country': 'Kenya',
                'description': 'Demonstration organisation. Not a real institution.',
            },
        )

        # ── Phase 1 — Signals ─────────────────────────────────────────────────
        s1, _ = IntelligenceSignal.objects.get_or_create(
            title='Nairobi Water Resilience Signal',
            defaults={
                'category': IntelligenceSignal.Category.WATER,
                'status': IntelligenceSignal.Status.OBSERVED,
                'location': 'Nairobi, Kenya',
                'source': DEMO_NOTE,
                'latitude': -1.286389,
                'longitude': 36.817223,
                'organisation': org_water,
                'description': (
                    'Demonstration signal. Tracks emerging water-stress indicators across '
                    'Nairobi metropolitan supply zones. Not based on verified real-world measurements.'
                ),
            },
        )
        s2, _ = IntelligenceSignal.objects.get_or_create(
            title='Nairobi Infrastructure Disruption',
            defaults={
                'category': IntelligenceSignal.Category.INFRASTRUCTURE,
                'status': IntelligenceSignal.Status.REVIEWING,
                'location': 'Nairobi, Kenya',
                'source': DEMO_NOTE,
                'latitude': -1.292066,
                'longitude': 36.821945,
                'organisation': org_sanctum,
                'description': (
                    'Demonstration signal. Surface transport and access patterns that may require '
                    'coordinated action. Not based on verified real-world measurements.'
                ),
            },
        )
        s3, _ = IntelligenceSignal.objects.get_or_create(
            title='Nakuru Ecological Restoration Opportunity',
            defaults={
                'category': IntelligenceSignal.Category.ECOLOGY,
                'status': IntelligenceSignal.Status.ACTIONABLE,
                'location': 'Nakuru, Kenya',
                'source': DEMO_NOTE,
                'latitude': -0.303099,
                'longitude': 36.080026,
                'organisation': org_sanctum,
                'description': (
                    'Demonstration signal. Identifies locations where ecological restoration '
                    'could create measurable resilience gains. Not based on verified real-world measurements.'
                ),
            },
        )
        s4, _ = IntelligenceSignal.objects.get_or_create(
            title='Kisumu Food Resilience Signal',
            defaults={
                'category': IntelligenceSignal.Category.FOOD,
                'status': IntelligenceSignal.Status.OBSERVED,
                'location': 'Kisumu, Kenya',
                'source': DEMO_NOTE,
                'latitude': -0.091702,
                'longitude': 34.767956,
                'organisation': org_water,
                'description': (
                    'Demonstration signal. Monitors food system stress indicators in the Lake Victoria '
                    'basin region. Not based on verified real-world measurements.'
                ),
            },
        )
        s5, _ = IntelligenceSignal.objects.get_or_create(
            title='Machakos Land Restoration Signal',
            defaults={
                'category': IntelligenceSignal.Category.ECOLOGY,
                'status': IntelligenceSignal.Status.VERIFIED,
                'location': 'Machakos, Kenya',
                'source': DEMO_NOTE,
                'latitude': -1.516667,
                'longitude': 37.266667,
                'organisation': org_sanctum,
                'description': (
                    'Demonstration signal. Tracks land degradation and restoration potential '
                    'in semi-arid zones. Not based on verified real-world measurements.'
                ),
            },
        )
        s6, _ = IntelligenceSignal.objects.get_or_create(
            title='Mombasa Coastal Energy Access',
            defaults={
                'category': IntelligenceSignal.Category.ENERGY,
                'status': IntelligenceSignal.Status.REVIEWING,
                'location': 'Mombasa, Kenya',
                'source': DEMO_NOTE,
                'latitude': -4.043477,
                'longitude': 39.668206,
                'organisation': org_sanctum,
                'description': (
                    'Demonstration signal. Examines renewable energy access gaps in coastal '
                    'communities. Not based on verified real-world measurements.'
                ),
            },
        )

        # ── Phase 2 — Evidence ────────────────────────────────────────────────
        Evidence.objects.get_or_create(
            title='Nairobi Water Stress Field Observation (Demo)',
            signal=s1,
            defaults={
                'evidence_type': Evidence.EvidenceType.OBSERVATION,
                'reliability': Evidence.Reliability.PLAUSIBLE,
                'description': 'Demonstration evidence record. Simulated field observation of reduced water pressure in supply zones. Not real data.',
            },
        )
        Evidence.objects.get_or_create(
            title='Municipal Supply Report Q3 (Demo)',
            signal=s1,
            defaults={
                'evidence_type': Evidence.EvidenceType.REPORT,
                'reliability': Evidence.Reliability.UNVERIFIED,
                'description': 'Demonstration evidence record. Simulated municipal report. Not real data.',
            },
        )
        Evidence.objects.get_or_create(
            title='Nakuru Vegetation Survey (Demo)',
            signal=s3,
            defaults={
                'evidence_type': Evidence.EvidenceType.DATA,
                'reliability': Evidence.Reliability.CONFIRMED,
                'description': 'Demonstration evidence record. Simulated vegetation survey data. Not real data.',
            },
        )

        # ── Phase 5 — Assessments ─────────────────────────────────────────────
        Assessment.objects.get_or_create(
            signal=s1,
            defaults={
                'summary': 'Demonstration assessment. Water stress indicators suggest elevated risk in northern supply zones. Coordinated monitoring recommended. Not based on real analysis.',
                'priority': Assessment.Priority.HIGH,
                'recommendation': 'Demonstration recommendation. Establish regular monitoring cadence and engage municipal water authority. Not real guidance.',
                'assessed_by': 'Atlas Sanctum Demo Analyst',
            },
        )
        Assessment.objects.get_or_create(
            signal=s3,
            defaults={
                'summary': 'Demonstration assessment. Ecological restoration potential is high based on simulated vegetation data. Not based on real analysis.',
                'priority': Assessment.Priority.MEDIUM,
                'recommendation': 'Demonstration recommendation. Identify community partners for pilot restoration programme. Not real guidance.',
                'assessed_by': 'Atlas Sanctum Demo Analyst',
            },
        )

        # ── Phase 4 — Opportunities ───────────────────────────────────────────
        opp1, _ = Opportunity.objects.get_or_create(
            title='Nairobi Water Monitoring Programme (Demo)',
            signal=s1,
            defaults={
                'status': Opportunity.OpportunityStatus.READY,
                'location': 'Nairobi, Kenya',
                'description': 'Demonstration opportunity. Establish a community-based water monitoring network. Not a real programme.',
            },
        )
        opp2, _ = Opportunity.objects.get_or_create(
            title='Nakuru Restoration Pilot (Demo)',
            signal=s3,
            defaults={
                'status': Opportunity.OpportunityStatus.SCOPING,
                'location': 'Nakuru, Kenya',
                'description': 'Demonstration opportunity. Pilot ecological restoration on degraded land parcels. Not a real programme.',
            },
        )

        # ── Phase 7 — Actions ─────────────────────────────────────────────────
        action1, _ = ActionItem.objects.get_or_create(
            title='Deploy water sensors at 5 sites (Demo)',
            opportunity=opp1,
            defaults={
                'status': ActionItem.ActionStatus.ASSIGNED,
                'assigned_to': 'Demo Field Team',
                'description': 'Demonstration action. Install low-cost water pressure sensors. Not a real task.',
            },
        )
        action2, _ = ActionItem.objects.get_or_create(
            title='Community stakeholder meeting (Demo)',
            opportunity=opp1,
            defaults={
                'status': ActionItem.ActionStatus.COMPLETE,
                'assigned_to': 'Demo Coordination Team',
                'description': 'Demonstration action. Convene community representatives to discuss monitoring programme. Not a real event.',
            },
        )
        action3, _ = ActionItem.objects.get_or_create(
            title='Identify restoration land parcels (Demo)',
            opportunity=opp2,
            defaults={
                'status': ActionItem.ActionStatus.IN_PROGRESS,
                'assigned_to': 'Demo Research Team',
                'description': 'Demonstration action. Map candidate land parcels for restoration pilot. Not a real task.',
            },
        )

        # ── Phase 8 — Impact Records ──────────────────────────────────────────
        ImpactRecord.objects.get_or_create(
            title='Community engagement milestone (Demo)',
            action=action2,
            defaults={
                'impact_type': ImpactRecord.ImpactType.SOCIAL,
                'metric': '120 community members reached (simulated)',
                'description': 'Demonstration impact record. Simulated outcome of stakeholder meeting. Not real data.',
            },
        )
        ImpactRecord.objects.get_or_create(
            title='Institutional partnership formed (Demo)',
            action=action2,
            defaults={
                'impact_type': ImpactRecord.ImpactType.INSTITUTIONAL,
                'metric': '2 partner organisations engaged (simulated)',
                'description': 'Demonstration impact record. Simulated institutional outcome. Not real data.',
            },
        )

        self.stdout.write(self.style.SUCCESS('Demo data seeded for all roadmap phases.'))
