from django.urls import path
from . import views

app_name = 'observatory'

urlpatterns = [
    # Phase 1
    path('', views.home, name='home'),
    path('signals/', views.signals, name='signals'),
    path('signals/<int:pk>/', views.signal_detail, name='signal_detail'),
    path('about/', views.about, name='about'),

    # Phase 2 — Evidence
    path('signals/<int:signal_pk>/evidence/', views.evidence_list, name='evidence_list'),
    path('signals/<int:signal_pk>/evidence/<int:pk>/', views.evidence_detail, name='evidence_detail'),

    # Phase 3 — Geospatial
    path('map/', views.signal_map, name='signal_map'),

    # Phase 4 — Opportunities
    path('opportunities/', views.opportunity_list, name='opportunity_list'),
    path('opportunities/<int:pk>/', views.opportunity_detail, name='opportunity_detail'),

    # Phase 5 — Assessment
    path('signals/<int:signal_pk>/assessment/', views.assessment_detail, name='assessment_detail'),

    # Phase 7 — Actions
    path('actions/', views.action_list, name='action_list'),
    path('actions/<int:pk>/', views.action_detail, name='action_detail'),

    # Phase 8 — Impact
    path('impact/', views.impact_list, name='impact_list'),

    # Phase 9 — Organisations
    path('organisations/', views.organisation_list, name='organisation_list'),
    path('organisations/<int:pk>/', views.organisation_detail, name='organisation_detail'),
]
