from django.urls import path
from .views import AtendimentoListView, AtendimentoDetailView


urlpatterns = [
    path('', AtendimentoListView.as_view()),
    path('<int:pk>/', AtendimentoDetailView.as_view()),
 
]
