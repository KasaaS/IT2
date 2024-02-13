import random
from os import system
system("clear")



def main():
    print("--- Velkommen til troskapstesten ---\n")
    spiller1 = 0
    spiller2 = 0
    for i in range(500):
        resultat = spill(usikker, halvveis)
        spiller1 += resultat[0]
        spiller2 += resultat[1]
    print(spiller1, spiller2)


def snill(beløp):
    # funksjon for snill strategi
    return "behold"

def slem(beløp):
    # funksjon for slem strategi
    return "kast"

def halvveis(beløp):
    if beløp >= 150000:
        return "kast"
    else:
        return "behold"


def usikker(beløp):
    # en funksjon for en spiller som 30% av gangene kaster kula når beløpet er under 50000
    # og kaster 70% av gangene når beløpet er 50000 eller mer
    tilfeldig_tall = random.randint(1,100)
    if beløp > 50000:
        if tilfeldig_tall <= 30:
            return "kast"
        else:
            return "behold"
    else:
        if tilfeldig_tall <= 70:
            return "kast"
        else:
            return "behold"
        

def veldig_usikker(beløp):
    tilfeldig_tall = random.randint(1,100)
    if tilfeldig_tall <= 50:
        return "behold"
    else:
        return "kast"






def spill(strategi1, strategi2):
    # En funksjon som spiller troskapspillet fra paradise hotell
    # Funksjonen returnerer en liste med gevinsten til hver spiller
    # f.eks [100000,0] eller [150000, 150000] eller [0, 80000] og så videre

    pott = 0 # potten er 0 i starten
    for i in range(30):
        pott += 10000 # øker potten
        if strategi1(pott) == "kast":
            return [pott, 0]
        elif strategi2(pott) == "kast":
            return [0, pott]


    return [pott/2, pott/2] # ingen kasta kula


main()