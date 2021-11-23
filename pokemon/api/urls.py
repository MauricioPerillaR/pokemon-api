from django.urls import path
from .views import PokemonDetailView

urlpatterns = [
    path('pokemon/<str:name>', PokemonDetailView.as_view())
]