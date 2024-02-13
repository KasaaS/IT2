import pygame
from os import system
system("clear")


# 1. Oppsett (init)
pygame.init() # Starter opp pygame
vindu = pygame.display.set_mode([300, 300])
klokke = pygame.time.Clock() # lager en klokke som begrenser spillet til antall fps jeg ønsker

x = 20
y = 30

spiller = True
while spiller: # gameloop
    # 2. Håndtere input/hendelser
    hendelser = pygame.event.get() # lager en liste med alle hendelsene
    for hendelse in hendelser:
        if hendelse.type == pygame.QUIT:
            spiller = False


    # 3. oppdater spill
    x += 1
    y += 1

    # 4. tegn (rendering)
    pygame.draw.circle(vindu, [255,255,255], [130,y], 20)
    pygame.draw.circle(vindu, [255,255,255], [110,20], 20)
    pygame.draw.circle(vindu, [255,255,255], [150,20], 20)
    pygame.display.update()

    klokke.tick(60) # forteller at løkka kun skal kjøre 60 ganger i sekundet (60 FPS)