from planet import Planet
import pygame
import random
from os import system

system("clear")


# Jeg bruker bare edd bildene. Klasser er over oppsett.



# 1. Oppsett

pygame.init()
BREDDE = 1000
HOYDE = 400
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

planeter = [
    Planet(50 ,200, 50, "bilder2/plank.png"),         
    Planet(150, 200, 100, "bilder2/plank.png"),  
    Planet(300, 200, 20, "bilder2/plank.png"),  
    Planet(400, 200, 40, "bilder2/plank.png"),
    Planet(500, 200, 45, "bilder2/plank.png"),
    Planet(600, 200, 10, "bilder2/plank.png"),
    Planet(700, 200, 25, "bilder2/plank.png"),
    Planet(800, 200, 30, "bilder2/plank.png")
]

# Jorda = Planet(100 ,200, 50, "bilder2/plank.png")        Oppretter et objekt av klassen planet


while True:

    # 2. Oppsett
    
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    # 3. Oppdater spill
    # 4. Tegn

    for p in planeter:
        p.tegn(vindu)

    pygame.display.flip()
    klokke.tick(FPS)