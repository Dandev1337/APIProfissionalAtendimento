from django.urls import path
from .views import ProfissionalListView, ProfissionalDetailView

urlpatterns = [
    path('', ProfissionalListView.as_view()),
    path('<int:pk>/', ProfissionalDetailView.as_view()),
    ]