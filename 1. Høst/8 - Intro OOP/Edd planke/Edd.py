import pygame
import random
from os import system

system("clear")


# 1. oppsett

pygame.init() # starter pygame programmet

BREDDE = 600
HOYDE = 600
FPS = 60

vindu = pygame.display.set_mode((BREDDE, HOYDE)) # Kode for å sette opp vinduet og størrelsen
klokke = pygame.time.Clock() # Vi definerer fps og setter det inn i klokke.

# Laster inn skrifttyper
overskrift_font = pygame.font.SysFont("Arial", 32)
overskrift_surface = overskrift_font.render("Plankthrower", True, "black")


# Lager spiller og definerer størrelse

pl1_surface = pygame.image.load("bilder2/pl1.png").convert_alpha() # laster spiller og gjør bakgrunn usynllig
pl1_surface = pygame.transform.scale_by(pl1_surface, 0.1)
pl1_rect = pl1_surface.get_rect() # endrer på verdier for hvor de skal stå
pl1_rect.bottom = HOYDE - 20
pl1_rect.centerx = BREDDE/2

pl2_surface = pygame.image.load("bilder2/pl2.png").convert_alpha() # laster spiller og gjør bakgrunn usynllig
pl2_surface = pygame.transform.scale_by(pl2_surface, 0.2)
pl2_rect = pl2_surface.get_rect() # endrer på verdier for hvor de skal stå
pl2_rect.top = 20
pl2_rect.centerx = BREDDE/2

planke_surface = pygame.image.load("bilder2/plank.png").convert_alpha()
planke_surface = pygame.transform.scale_by(planke_surface, 0.1)
planke_rect = planke_surface.get_rect()
planke_rect.top = pl2_rect.bottom
planke_rect.centerx = pl2_rect.centerx

planke2_surface = pygame.image.load("bilder2/plank.png").convert_alpha()
planke2_surface = pygame.transform.scale_by(planke2_surface, 0.1)
planke2_rect = planke2_surface.get_rect()
planke2_rect.top = pl2_rect.bottom
planke2_rect.centerx = pl2_rect.centerx

planke3_surface = pygame.image.load("bilder2/plank.png").convert_alpha()
planke3_surface = pygame.transform.scale_by(planke3_surface, 0.1)
planke3_rect = planke3_surface.get_rect()
planke3_rect.top = pl2_rect.bottom
planke3_rect.centerx = pl2_rect.centerx


# Ulike farter
pl2_xfart = 2

pl1_xfart = 0
pl1_yfart = 0

planke_fart = 5
planke2_fart = 6
planke3_fart = 7


while True:

    # 2. Input
    for hendelse in pygame.event.get(): # Henter hendelser vi gjør, f.eks trykke på en knapp.

        if hendelse.type == pygame.QUIT: # Når vi trykker kryss, lukker vi programmet
            pygame.quit()
            raise SystemExit
        
        if hendelse.type == pygame.KEYDOWN: # Bestemmer hvordan vi skal bevege oss basert på taster

            if hendelse.key == pygame.K_UP or hendelse.key == pygame.K_w:
                pl1_yfart = -3      
            elif hendelse.key == pygame.K_LEFT or hendelse.key == pygame.K_a:
                pl1_xfart = -3
            elif hendelse.key == pygame.K_DOWN or hendelse.key == pygame.K_s:
                pl1_yfart = 3
            elif hendelse.key == pygame.K_RIGHT or hendelse.key == pygame.K_d:
                pl1_xfart = 3


        if hendelse.type == pygame.KEYUP:

            if hendelse.key == pygame.K_UP or hendelse.key == pygame.K_w:
                pl1_yfart = 0          
            elif hendelse.key == pygame.K_LEFT or hendelse.key == pygame.K_a:
                pl1_xfart = 0
            elif hendelse.key == pygame.K_DOWN or hendelse.key == pygame.K_s:
                pl1_yfart = 0
            elif hendelse.key == pygame.K_RIGHT or hendelse.key == pygame.K_d:
                pl1_xfart = 0



        
    # 3. Oppdater spill

    # Bestemmer hvordan johnny 2x4 skal bevege seg
    pl2_rect.left -= pl2_xfart
    if pl2_rect.left < 0 or pl2_rect.right > BREDDE:
        pl2_xfart *= -1


    pl1_rect.left += pl1_xfart
    pl1_rect.top += pl1_yfart
    

    planke_rect.top += planke_fart

    if planke_rect.top > HOYDE:
        planke_rect.top = pl2_rect.bottom
        planke_rect.centerx = pl2_rect.centerx
        if planke_fart < 10:
            planke_fart = planke_fart + 0.2

    planke2_rect.top += planke2_fart

    if planke2_rect.top > HOYDE:
        planke2_rect.top = pl2_rect.bottom
        planke2_rect.centerx = pl2_rect.centerx
        if planke2_fart < 10:
            planke2_fart = planke2_fart + 0.5

    planke3_rect.top += planke3_fart

    if planke3_rect.top > HOYDE:
        planke3_rect.top = pl2_rect.bottom
        planke3_rect.centerx = pl2_rect.centerx
        if planke3_fart < 10:
            planke3_fart = planke3_fart + 0.8


    if pl1_rect.colliderect(planke_rect):
        pygame.quit()
        raise SystemExit
    if pl1_rect.colliderect(planke2_rect):
        pygame.quit()
        raise SystemExit
    if pl1_rect.colliderect(planke3_rect):
        pygame.quit()
        raise SystemExit

    # 4. Tegn
    vindu.fill("white") # bakgrunnsfarge
    vindu.blit(overskrift_surface, (10,10)) # blit legger noe til på vinduet, eller på "surface", vi setter x og y kordinater

    vindu.blit(planke_surface, planke_rect)
    vindu.blit(planke2_surface, planke2_rect)
    vindu.blit(planke3_surface, planke3_rect)


    # får inn spillere
    vindu.blit(pl1_surface, pl1_rect)
    vindu.blit(pl2_surface, pl2_rect)

    pygame.display.flip() #oppdaterer vinduet.
    klokke.tick(FPS) # her sier vi hva fps skal være