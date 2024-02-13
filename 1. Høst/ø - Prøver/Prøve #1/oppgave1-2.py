import random
from os import system
system("clear")


# Oppgave 1.1
terningkast = random.randint(1,6)
print("Resultatet på et terningkast er", terningkast, "\n")



# Oppgave 1.2
kasteliste = []
for i in range(0,5):
    terningkast = random.randint(1,6)
    kasteliste.append(terningkast)

print("Reslutatet av 5 terningkast er som følger:")
print(kasteliste)
print()




# Oppgave 1.3 A)
antall_kast = int(input("Hvor mange terninger ønsker du å kaste? \n"))



# Oppgave 1 B)
def kast_terninger(x):
    liste = []
    while x > 0:
        x -= 1
        terningkast = random.randint(1,6)
        liste.append(terningkast)
    return liste


 # Oppgave 1 C)
print("\nResultatet av", antall_kast, "kast er som følger:")
print(kast_terninger(antall_kast))
print() # bare for å gjøre ryddigere når du kjører i ett




# Oppgave 2)
dato = input("skriv en dato i ISO format \n")
år, måned, dag = dato.split(".")
print("\nDatoen din i Norsk standard blir", dag+ "." + måned + "." + år + "\n")