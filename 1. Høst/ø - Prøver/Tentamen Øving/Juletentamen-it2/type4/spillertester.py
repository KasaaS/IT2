from spiller import Spiller

print("-- Spillertester --")
print()

spiller1 = Spiller("Ada Hegerberg")
spiller2 = Spiller("Guro Reiten")
spiller3 = Spiller("Maren Mjelde")

assert spiller1.hent_navn() == "Ada Hegerberg"
print(".hent_navn(): OK!")

assert spiller2.hent_kamper() == 0
spiller2.spill_kamp()
assert spiller2.hent_kamper() == 1
print(".spill_kamp(): OK!")
print(".hent_kamper(): OK!")

assert spiller3.sjekk_navn("Maren Mjelde") == True
assert spiller3.sjekk_navn("Mjelde") == True
assert spiller3.sjekk_navn("Maren") == True
assert spiller3.sjekk_navn("Mren") == False
print(".sjekk_navn(): OK!")

print()
print("0 feil!")
