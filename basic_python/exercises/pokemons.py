Bulbasaur = {'CP': 100, 'HP': 20 }
Rattata = {'CP': 30, 'HP': 10} 
Pikachu = {'CP': 120, 'HP': 120}
Raichu = {'CP': 150, 'HP':160}

pokeball = {
    'pokemons_count': 3,
    'pokemons': {
        'Bulbasaur': Bulbasaur, 
        'Rattata': Rattata, 
        'Pikachu': Pikachu,
        'Raichu': Raichu,
    },
    'points': 100, 
}

print(pokeball)
# list all pokemons' names
print(pokeball['pokemons'].keys())

# remove ratta
pokeball['pokemons'].pop('Rattata')
print(pokeball)

# Create new Raichu pokemon with stats: CP = 150, HP = 160
print(pokeball)

# Find pokemon with highest CP parameter
# first basic solution, not pythonic
curr_max_cp = 0
pokemon_max_cp = None
for pokemon, stats in pokeball['pokemons'].items():
    if stats['CP'] > curr_max_cp:
        curr_max_cp = stats['CP']
        pokemon_max_cp = pokemon
print(pokemon_max_cp)

# second solution, pythonic way
from operator import itemgetter
print(max(pokeball['pokemons'].iteritems(), key=lambda (k,v): itemgetter('CP')(v)))

# Update points in pokeball, points it is just sum of all CP parameters divide by pokemons count

points = 0
for pokemon, stats in pokeball['pokemons'].items():
    points += stats['CP']

pokeball['points'] = points/len(pokeball['pokemons'])
print(points)
print(pokeball)
