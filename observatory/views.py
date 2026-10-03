from django.shortcuts import render


def home(request):
    signals = [
        {
            'title': 'Water resilience',
            'category': 'Water',
            'status': 'Monitor',
            'description': 'Track emerging water-stress signals and infrastructure needs.',
        },
        {
            'title': 'Urban mobility',
            'category': 'Infrastructure',
            'status': 'Observed',
            'description': 'Surface transport and access patterns that may require coordinated action.',
        },
        {
            'title': 'Restoration opportunity',
            'category': 'Ecology',
            'status': 'Opportunity',
            'description': 'Identify locations where ecological restoration could create measurable resilience.',
        },
    ]
    context = {
        'signals': signals,
        'principles': ['Observe', 'Understand', 'Decide', 'Coordinate', 'Learn'],
    }
    return render(request, 'observatory/home.html', context)
