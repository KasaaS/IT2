import pygame
import random
from os import system

system("clear")

# Gameloop mal

# 1. Oppsett
pygame.init()

BREDDE = 1000
HOYDE = 600
vindu = pygame.display.set_mode((BREDDE,HOYDE))

FPS = 60
klokke = pygame.time.Clock()

pygame.display.set_caption('Mitt spill') # Navn på vinduet
font = pygame.font.SysFont("Arial", 32) # Skrifttype
font2 = pygame.font.SysFont("Arial", 12) # Skrifttype 2

dino_x = 450
dino_y = 300
dino_bilde1 = pygame.image.load("bilder/dino1.png").convert_alpha() # laster inn bilde


tre1_x = random.randint(100,900)
tre1_y = random.randint(100,500)
tre1_tilstand = "levende"

tre2_x = random.randint(100,900)
tre2_y = random.randint(100,500)
tre2_tilstand = "levende"

tre3_x = random.randint(100,900)
tre3_y = random.randint(100,500)
tre3_tilstand = "levende"

tre_bilde1 = pygame.image.load("bilder/tre1.png").convert_alpha()
tre_bilde2 = pygame.image.load("bilder/tre2.png").convert_alpha()


while True:

    # 2. Håndter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    taster = pygame.key.get_pressed()
    if taster[pygame.K_RIGHT] or taster[pygame.K_d]:
        dino_x += 3
    taster = pygame.key.get_pressed()
    if taster[pygame.K_LEFT] or taster[pygame.K_a]:
        dino_x -= 3
    taster = pygame.key.get_pressed()
    if taster[pygame.K_UP] or taster[pygame.K_w]:
        dino_y -= 3
    taster = pygame.key.get_pressed()
    if taster[pygame.K_DOWN] or taster[pygame.K_s]:
        dino_y += 3


    if taster[pygame.K_ESCAPE]:
        pygame.quit()
        raise SystemExit

    # 3. Oppdater spill
    dino_rektangel = pygame.Rect(dino_x,dino_y,100,100)

    tre1_rektangel = pygame.Rect(tre1_x,tre1_y,40,70)
    tre2_rektangel = pygame.Rect(tre2_x,tre2_y,40,70)
    tre3_rektangel = pygame.Rect(tre3_x,tre3_y,80,70)

    if dino_rektangel.colliderect(tre1_rektangel):
        tre1_tilstand = "død"

    if dino_rektangel.colliderect(tre2_rektangel):
        tre2_tilstand = "død"

    if dino_rektangel.colliderect(tre3_rektangel):
        tre3_tilstand = "død"

    # 4. Tegn
    vindu.fill("gray")

    vindu.blit(dino_bilde1, (dino_x,dino_y))

    tekst_lykke_til = font.render("DINO", True, "black")
    vindu.blit(tekst_lykke_til,(450,100))

    if tre1_tilstand == "levende":
        vindu.blit(tre_bilde1, (tre1_x,tre1_y))
    if tre2_tilstand == "levende":
        vindu.blit(tre_bilde1, (tre2_x,tre2_y))
    if tre3_tilstand == "levende":
        vindu.blit(tre_bilde2, (tre3_x,tre3_y))

    # #Oppgave: Lag flagg 
    # pygame.draw.rect(vindu, (255,0,0), (100,100, 300,200))
    # pygame.draw.rect(vindu, (255,255,255),(100,180, 300,40))
    # pygame.draw.rect(vindu, (255,255,255),(180,100, 40,200))

    pygame.display.flip()
    klokke.tick(FPS)