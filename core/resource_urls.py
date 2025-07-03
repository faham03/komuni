# core/resource_urls.py (ou ajoute dans core/urls.py selon ton organisation)

from django.urls import path
from .views import (
    ResourceListCreateView,
    ResourceDetailView,
    ResourceUpdateView,
    ResourceDeleteView,
)

urlpatterns = [
    path('resources/', ResourceListCreateView.as_view(), name='resource-list-create'),
    path('resources/<int:pk>/', ResourceDetailView.as_view(), name='resource-detail'),
    path('resources/<int:pk>/edit/', ResourceUpdateView.as_view(), name='resource-update'),
    path('resources/<int:pk>/delete/', ResourceDeleteView.as_view(), name='resource-delete'),
]
