import os
import platform


# Quiz med ett spørsmål


def rens_terminal():
    if platform.system == "win32":
        os.system("cls")
    else:
        os.system("clear")
 


while True: 
    rens_terminal()

    print("-- Quiz --")
    print()


    print("Spørsmål 1.")
    print("hvor mange spørsmål har du svar på så langt?") 

    riktig = "a"

    print("A: 0")
    print("B: 2")
    print("C: 1")
    print("D: 4")

    svar = input("> ")

    if riktig == svar.lower():
        print("Riktig svar")
        input("Enter for å spille igjen")
    else:
        input("Feil svar. Enter for å spille igjen.")