import pygame
import random
from os import system
system("clear")

def tilfeldig_farge():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return [r, b, g]

# 1. Oppsett (init)
pygame.init() # Starter opp pygame
BREDDE = 1200
HOYDE = 600
vindu = pygame.display.set_mode([BREDDE, HOYDE])
klokke = pygame.time.Clock() # lager en klokke som begrenser spillet til antall fps jeg ønsker

x = 100
y = 200

radius = 20
farge = tilfeldig_farge() # gir tilfeldig farge

x_fart = 2
y_fart = 2


spiller = True
while spiller: # gameloop
    # 2. Håndtere input/hendelser
    hendelser = pygame.event.get() # lager en liste med alle hendelsene
    for hendelse in hendelser:
        if hendelse.type == pygame.QUIT:
            spiller = False


    # 3. oppdater spill
    x += x_fart
    y += y_fart

    if x > BREDDE - radius or x < radius:
        x_fart = x_fart * -1
        farge = tilfeldig_farge()

    if y > HOYDE - radius or y < radius:
        y_fart = y_fart * -1
        farge = tilfeldig_farge()



    # 4. tegn (rendering)
    vindu.fill([0,0,0])
    pygame.draw.circle(vindu, farge, [x,y], radius)
    pygame.display.update()

    klokke.tick(60) # forteller at løkka kun skal kjøre 60 ganger i sekundet (60 FPS)