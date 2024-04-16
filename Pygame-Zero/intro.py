# Må installere pygame-zero i terminalen
# mac: python -m pip install pgzero
# Win: python3 -m pip install pgzero

import pgzrun

WIDTH = 600     # Skriver width og height - definerer uten å skrive noe mer
HEIGHT = 600

def draw():     # Tegner uten å gjøre noe
    screen.fill((255,0,0))

pgzrun.go() # For å kjøre ett vindu