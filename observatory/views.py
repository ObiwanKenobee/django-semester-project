from django.shortcuts import render, get_object_or_404
from .models import IntelligenceSignal


def home(request):
    signals = IntelligenceSignal.objects.all()[:6]
    context = {
        'signals': signals,
        'principles': ['Observe', 'Understand', 'Decide', 'Coordinate', 'Learn'],
    }
    return render(request, 'observatory/home.html', context)


def signals(request):
    all_signals = IntelligenceSignal.objects.all()
    return render(request, 'observatory/signals.html', {'signals': all_signals})


def signal_detail(request, pk):
    signal = get_object_or_404(IntelligenceSignal, pk=pk)
    return render(request, 'observatory/signal_detail.html', {'signal': signal})


def about(request):
    return render(request, 'about.html')
