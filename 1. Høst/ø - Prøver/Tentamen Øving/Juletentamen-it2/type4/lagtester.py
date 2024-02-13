print("-- Lagtester --")
print()

from lag import Lag
from spiller import Spiller

lag1 = Lag("Rosenborg")
assert lag1.hent_navn() == "Rosenborg"
print(".hent_navn(): OK!")

lag2 = Lag("Stabæk")
assert lag2.hent_poeng() == 0
lag2.seier()
assert lag2.hent_poeng() == 3
print(".seier(): OK!")
lag2.uavgjort()
assert lag2.hent_poeng() == 4
print(".uavgjort(): OK!")
lag2.tap()
assert lag2.hent_poeng() == 4
print(".tap(): OK!")
print(".hent_poeng(): OK!")


lag3 = Lag("Vålerenga")
spiller1 = Spiller("Osame Sahraoui")
spiller2 = Spiller("Odin Thiago Holm")
lag3.legg_til_spiller(spiller1)
lag3.legg_til_spiller(spiller2)
lag3.spill_kamp()
assert spiller1.hent_kamper() == 1
assert spiller2.hent_kamper() == 1
print(".legg_til_spiller(): OK!")
print(".spill_kamp(): OK!")
print(".hent_kamper(): OK!")

assert lag3.finn_spiller("Osame") == spiller1
assert lag3.finn_spiller("Holm") == spiller2
print(".finn_spiller(): OK!")

print()
print("0 feil!")