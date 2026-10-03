from django.core.management.base import BaseCommand
from observatory.models import IntelligenceSignal

DEMO_SIGNALS = [
    {
        'title': 'Nairobi Water Resilience Signal',
        'category': IntelligenceSignal.Category.WATER,
        'status': IntelligenceSignal.Status.OBSERVED,
        'location': 'Nairobi, Kenya',
        'source': 'Demo / Simulated',
        'description': (
            'Demonstration signal. Tracks emerging water-stress indicators across '
            'Nairobi metropolitan supply zones. Not based on verified real-world measurements.'
        ),
    },
    {
        'title': 'Nairobi Infrastructure Disruption',
        'category': IntelligenceSignal.Category.INFRASTRUCTURE,
        'status': IntelligenceSignal.Status.REVIEWING,
        'location': 'Nairobi, Kenya',
        'source': 'Demo / Simulated',
        'description': (
            'Demonstration signal. Surface transport and access patterns that may require '
            'coordinated action. Not based on verified real-world measurements.'
        ),
    },
    {
        'title': 'Nakuru Ecological Restoration Opportunity',
        'category': IntelligenceSignal.Category.ECOLOGY,
        'status': IntelligenceSignal.Status.ACTIONABLE,
        'location': 'Nakuru, Kenya',
        'source': 'Demo / Simulated',
        'description': (
            'Demonstration signal. Identifies locations where ecological restoration '
            'could create measurable resilience gains. Not based on verified real-world measurements.'
        ),
    },
    {
        'title': 'Kisumu Food Resilience Signal',
        'category': IntelligenceSignal.Category.FOOD,
        'status': IntelligenceSignal.Status.OBSERVED,
        'location': 'Kisumu, Kenya',
        'source': 'Demo / Simulated',
        'description': (
            'Demonstration signal. Monitors food system stress indicators in the Lake Victoria '
            'basin region. Not based on verified real-world measurements.'
        ),
    },
    {
        'title': 'Machakos Land Restoration Signal',
        'category': IntelligenceSignal.Category.ECOLOGY,
        'status': IntelligenceSignal.Status.VERIFIED,
        'location': 'Machakos, Kenya',
        'source': 'Demo / Simulated',
        'description': (
            'Demonstration signal. Tracks land degradation and restoration potential '
            'in semi-arid zones. Not based on verified real-world measurements.'
        ),
    },
    {
        'title': 'Mombasa Coastal Energy Access',
        'category': IntelligenceSignal.Category.ENERGY,
        'status': IntelligenceSignal.Status.REVIEWING,
        'location': 'Mombasa, Kenya',
        'source': 'Demo / Simulated',
        'description': (
            'Demonstration signal. Examines renewable energy access gaps in coastal '
            'communities. Not based on verified real-world measurements.'
        ),
    },
]


class Command(BaseCommand):
    help = 'Seed the database with demonstration Intelligence Signals (clearly labelled as demo data).'

    def handle(self, *args, **options):
        created = 0
        for data in DEMO_SIGNALS:
            _, was_created = IntelligenceSignal.objects.get_or_create(
                title=data['title'],
                defaults=data,
            )
            if was_created:
                created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'Done. {created} new demo signal(s) created. '
                f'{len(DEMO_SIGNALS) - created} already existed.'
            )
        )
