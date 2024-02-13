from os import system


# Oppgave 1
system("clear")
match = 0

navn = input("Gi meg to navn med 'og' i mellom \n").lower()
navn1, navn2 = navn.split("og")


if len(navn1) == len(navn2):
    match = 60
elif navn1[0] == navn2[0]:
    match = 40
else:
    match = 15


# Oppgave 2
system("clear")
bosted = input("Gi meg bostedene deres med 'og' i mellom \n").lower()
bosted1, bosted2 = navn.split("og")

if bosted1 == bosted2:
    match = match*1.5



system("clear")
alder = input("Gi meg alderene deres med 'og' i mellom \n").lower()
alder1, alder2 = alder.split("og")

alder1 = int(alder1)
alder2 = int(alder2)

if alder1 == (alder2/2) + 7 or alder2 == (alder1/2) + 7:
    match = match/2
elif alder1 == alder2:
    match = match*1.1



# Oppgave 3

system("clear")
if "t" in navn1 or "t" in navn2:
    match = match +2
elif "a" in navn1 or "a" in navn2:
    match = match +2






print(f"Deres match er {match:.2f}%")
