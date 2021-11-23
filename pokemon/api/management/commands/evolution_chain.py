from django.core.management.base import BaseCommand, CommandParser
import requests


from api.models import Pokemon


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('id', type=int)
        
    def handle(self, *args, **options):
        evolution_chain = self.get_evolution_chain(options['id'])
        self.create_all_pokemon_of_evolution_chain(evolution_chain)
        

    def get_evolution_chain(self, id_chain):
        return requests.get('https://pokeapi.co/api/v2/evolution-chain/10').json()
    

    def create_all_pokemon_of_evolution_chain(self, evolution_chain):
        pokemons = self.get_pokemons_of_evolution_chain(evolution_chain)

        for pokemon in pokemons:
            pokemon_detail = self.get_pokemon_detail(pokemon['name'])
            pokemon_detail['evolutions'] = evolution_chain
            pokemon_detail['evolution_type'] = pokemon['evolution_type']

            Pokemon.objects.update_or_create(**pokemon_detail)
    
    
    def get_pokemons_of_evolution_chain(self, evolution_chain):
        evoChain = [
            {
                'name': evolution_chain['chain']['species']['name'],
                'evolution_type': self.get_evolution_type(bool(evolution_chain['chain']['evolves_to']))
            }
        ]

        def get_evolves(evolves_to):
            evoChain = []
            for evolve in evolves_to:
                canEvolve = bool(evolve['evolves_to'])
                name = evolve['species']['name']
                evolution_type = self.get_evolution_type(canEvolve)
                
                evoChain.append(
                    { 'name' : name, 'evolution_type': evolution_type }
                    )
                
                if canEvolve:
                    evoChain.extend(get_evolves(evolve['evolves_to']))

            return evoChain

        evoChain.extend(get_evolves(evolution_chain['chain']['evolves_to']))

        return evoChain


    def get_evolution_type(self, canEvolve):
        if canEvolve:
            return 'Preevolution'
        else:
            return 'Evolution'


    def get_pokemon_detail(self, pokemon_name):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}').json()
        pokemon = {
            'name' : pokemon_name,
            'height': response['height'],
            'weight': response['weight'],
            'stats': response['stats']
        }

        return pokemon
    
        

    




