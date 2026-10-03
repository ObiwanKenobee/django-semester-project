from django.shortcuts import render, get_object_or_404
from .models import (
    IntelligenceSignal, Evidence, Assessment,
    Opportunity, ActionItem, ImpactRecord, Organisation,
)


# ── Phase 1 ──────────────────────────────────────────────────────────────────

def home(request):
    signals = IntelligenceSignal.objects.all()[:6]
    context = {
        'signals': signals,
        'principles': ['Observe', 'Understand', 'Decide', 'Coordinate', 'Learn'],
    }
    return render(request, 'observatory/home.html', context)


def signals(request):
    category = request.GET.get('category', '')
    status = request.GET.get('status', '')
    qs = IntelligenceSignal.objects.all()
    if category:
        qs = qs.filter(category=category)
    if status:
        qs = qs.filter(status=status)
    context = {
        'signals': qs,
        'categories': IntelligenceSignal.Category.choices,
        'statuses': IntelligenceSignal.Status.choices,
        'selected_category': category,
        'selected_status': status,
    }
    return render(request, 'observatory/signals.html', context)


def signal_detail(request, pk):
    signal = get_object_or_404(IntelligenceSignal, pk=pk)
    return render(request, 'observatory/signal_detail.html', {'signal': signal})


def about(request):
    return render(request, 'about.html')


# ── Phase 2 — Evidence ────────────────────────────────────────────────────────

def evidence_list(request, signal_pk):
    signal = get_object_or_404(IntelligenceSignal, pk=signal_pk)
    return render(request, 'observatory/evidence_list.html', {
        'signal': signal,
        'evidence': signal.evidence.all(),
    })


def evidence_detail(request, signal_pk, pk):
    signal = get_object_or_404(IntelligenceSignal, pk=signal_pk)
    item = get_object_or_404(Evidence, pk=pk, signal=signal)
    return render(request, 'observatory/evidence_detail.html', {'signal': signal, 'item': item})


# ── Phase 3 — Geospatial ──────────────────────────────────────────────────────

def signal_map(request):
    mapped = IntelligenceSignal.objects.exclude(latitude=None).exclude(longitude=None)
    return render(request, 'observatory/signal_map.html', {'signals': mapped})


# ── Phase 4 — Opportunities ───────────────────────────────────────────────────

def opportunity_list(request):
    opportunities = Opportunity.objects.select_related('signal').all()
    return render(request, 'observatory/opportunity_list.html', {'opportunities': opportunities})


def opportunity_detail(request, pk):
    opportunity = get_object_or_404(Opportunity, pk=pk)
    return render(request, 'observatory/opportunity_detail.html', {'opportunity': opportunity})


# ── Phase 5 — Assessment ──────────────────────────────────────────────────────

def assessment_detail(request, signal_pk):
    signal = get_object_or_404(IntelligenceSignal, pk=signal_pk)
    assessment = get_object_or_404(Assessment, signal=signal)
    return render(request, 'observatory/assessment_detail.html', {
        'signal': signal,
        'assessment': assessment,
    })


# ── Phase 7 — Action Items ────────────────────────────────────────────────────

def action_list(request):
    actions = ActionItem.objects.select_related('opportunity__signal').all()
    return render(request, 'observatory/action_list.html', {'actions': actions})


def action_detail(request, pk):
    action = get_object_or_404(ActionItem, pk=pk)
    return render(request, 'observatory/action_detail.html', {'action': action})


# ── Phase 8 — Impact ──────────────────────────────────────────────────────────

def impact_list(request):
    impacts = ImpactRecord.objects.select_related('action__opportunity__signal').all()
    return render(request, 'observatory/impact_list.html', {'impacts': impacts})


# ── Phase 9 — Organisations ───────────────────────────────────────────────────

def organisation_list(request):
    orgs = Organisation.objects.prefetch_related('signals').all()
    return render(request, 'observatory/organisation_list.html', {'organisations': orgs})


def organisation_detail(request, pk):
    org = get_object_or_404(Organisation, pk=pk)
    return render(request, 'observatory/organisation_detail.html', {'org': org})
