import json
from pokemon import Pokemon

with open("pokémon.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)

pokémon_liste = []
for pokémon_ordbok in data:
    ny_pokémon = Pokemon(pokémon_ordbok)
    pokémon_liste.append(ny_pokémon)

while True:
    print("-- Velkommen til Pokémon --")
    print("1. Se pokémonoversikt")
    print("2. Se treneroversikt")
    print("3. Lag trener")
    print("4. Avslutt")
    brukerinput = input("> ")

    if brukerinput == "1":
        print("Pokémonoversikt")
        for pokémon in pokémon_liste:
            print(pokémon)