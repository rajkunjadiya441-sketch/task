from itertools import combinations
print(list(comb))
pokedex = {
    'Pikachu': ('Electric',),
    'Charizard': ('Fire', 'Flying'),
    'Lapras': ('Water', 'Ice'),
    'Machamp': ('Fighting',),
    'Mewtwo': ('Psychic', 'Fighting'),
    'Hoopa': ('Psychic', 'Ghost', 'Dark'),
    'Lugia': ('Psychic', 'Flying', 'Water'),
    'Squirtle': ('Water',),
    'Gengar': ('Ghost', 'Poison'),
    'Onix': ('Rock', 'Ground')
}
def strongest_teams(pokedex,k):
 strongest=[]
 max=0
 for name in combinations(pokedex.keys(),3):
    typ=set() 
    for pokemon in name:
      typ.update(pokedex[pokemon])
    total=len(typ)
    if total > max:
      max=total
      strongest = [(name, typ)]
    elif max==total:
      strongest.append((name,typ))
 return strongest,max        
k=int(input("enter the no of squad mem"))
teams, max_types=strongest_teams(pokedex, k)
print(teams ,max_types)  
    
