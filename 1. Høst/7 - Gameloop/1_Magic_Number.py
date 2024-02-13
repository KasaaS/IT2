import pygame
import random
from os import system
system("clear")

# Gameloop mønsteret


    # 1. Oppsett
magisk_tall = random.randint(1,10)
antall_forsøk = 0

#Gameloop:
while True:

    # 2. Håndter input
    brukerinput = input("Hva er det magiske tallet?")
    if brukerinput == "avslutt":
        break
    tall = int(brukerinput)

    # 3. Oppdater spill
    antall_forsøk += 1

    # 4. Tegn (print)
    if tall > magisk_tall:
        print("For høyt")
    elif tall < magisk_tall:
        print("For lavt")
    else:
        print(f"Riktig! Antall forsøk: {antall_forsøk}")
        break