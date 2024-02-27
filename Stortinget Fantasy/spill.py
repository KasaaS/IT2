import os
import platform
import sys
import json # øverst i python-fila
from politiker import Politiker
from fantasiparti import Fantasiparti


with open("representanter.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)
representatner = data["dagensrepresentanter_liste"]


# oppretter en liste med politiker objekter (opretter av klassen)
politikere = []
for politiker_ordbok in representatner:
    ny_politiker = Politiker(politiker_ordbok)
    politikere.append(ny_politiker)





def rens_terminal():
    if platform.system == "win32":
        os.system("cls")
    else:
        os.system("clear")
 
 
print("-- Velkommen til stortinget fantasy --")

print()
print("Du må stifte et parti for å spille.")
print("Hva skal partiet ditt hete?") 
partinavn = input("> ")
print("Hva heter du?")
spillernavn = input("> ")
spillerparti = Fantasiparti(partinavn, spillernavn)
print(f"Gratulerer! Ditt nye parti med navn {partinavn} ble stiftet med partileder {spillernavn}")
input("Trykk enter for å starte spillet")


while True:
    rens_terminal()
    print("-- Stortinget-fantasy --")
    print("1: Politikeroversikt")
    print("2: vis mitt parti")
    print("3: Avslutt")
    brukervalg = input(">")
    
    if brukervalg == "1":
        print("-- Politikeroversikt --")
        for politiker in politikere:
            print(politiker)
        input("Trykk enter for å gå tilbake til hovedmenyen")

    elif brukervalg == "2":
        print("Mitt Parti")
        spillerparti.vis_parti()
        input("Trykk enter for å gå tilbake til hovedmenyen")
        
    elif brukervalg == "3":
        print("Avslutter..")
        break # bryter ut av while-løkken
    else:
        print("Ugyldig valg")