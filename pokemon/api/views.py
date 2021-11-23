from api.models import Pokemon
from django.views import generic
from django.http import JsonResponse
from django.forms import model_to_dict

# Create your views here.
class PokemonDetailView(generic.DetailView):
    def get(self, requests, name):
        try:
            pokemon = Pokemon.objects.get(name=name)
        except Pokemon.DoesNotExist:
            return JsonResponse({})

        return JsonResponse(model_to_dict(pokemon))
