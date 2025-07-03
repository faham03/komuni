from django.urls import path
from .views import ResourceListCreateView, ResourceDeleteView

urlpatterns = [
    path('resources/', ResourceListCreateView.as_view(), name='resource-list-create'),
    path('resources/<int:pk>/delete/', ResourceDeleteView.as_view(), name='resource-delete'),
]
