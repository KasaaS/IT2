# Funksjoner for sortering og printing av tabell
# Disse trenger du ikke bry deg om

def sorter_serie_bubble_sort(serie):
    tabell = serie.hent_lagliste().copy()
    n = len(tabell)
    for i in range(n):
        sortert = True
        for j in range(n - i - 1):
            if tabell[j].hent_poeng() < tabell[j + 1].hent_poeng():
                tabell[j], tabell[j + 1] = tabell[j + 1], tabell[j]
                sortert = False
        if sortert:
            break
    return tabell

def print_tabell(serie):
    print()
    print(f"-- {serie.hent_navn()} -- ")
    tabell = sorter_serie_bubble_sort(serie)
    print(f" #  {'Lag':<15} Poeng")
    for i, lag in enumerate(tabell):
        print(f"{i+1: >2}. {lag.hent_navn():<15} {lag.hent_poeng()}")
    print()

# -------------------


print("-- Serietester --")

from serie import Serie
from lag import Lag
from spiller import Spiller

pl = Serie("Premier League")

assert pl.hent_navn() == "Premier League"

arsenal = Lag("Arsenal")
arsenal.legg_til_spiller(Spiller("Martin Ødegaard"))
arsenal.legg_til_spiller(Spiller("Bukayo Saka"))

city = Lag("Manchester City")
city.legg_til_spiller(Spiller("Phil Foden"))
city.legg_til_spiller(Spiller("Erling Braut Haaland"))

pl.legg_til_lag(arsenal)
pl.legg_til_lag(city)

print_tabell(pl)

print("Spiller kamper")

pl.spill_kamp(arsenal, city, 3, 0)
print("Arsenal - Man City: 3 - 0")
pl.spill_kamp(arsenal, city, 3, 3)
print("Arsenal - Man City: 3 - 3")
print_tabell(pl)

assert arsenal.hent_poeng() == 4
assert city.hent_poeng() == 1
assert city.finn_spiller("Foden").hent_kamper() == 2

print()
print("0 feil!")

