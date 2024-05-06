import pygame

from spillebrett import Spillebrett
from meny import Meny


# Oppsett av pygame
pygame.init()
BREDDE = 800 # bredde på vinduet
HOYDE = 600  # høyde på vinduet
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
kjorer = True


## Endrer navn i toppen av vindu, samt fikser ikon - Bare for gøy :)
pygame.display.set_caption('Hjemmelaga pingpong')
ikon = pygame.image.load("ikon.png")
pygame.display.set_icon(ikon)



# OPPSETT AV SPILL HER:

## Oppretter brettene for meny og spill
spillebrett = Spillebrett(HOYDE, BREDDE)
menybrett = Meny(HOYDE, BREDDE)
menybrett.spill_aktiv = False


while kjorer:
    # fyll skjermen med en farge for å fjerne alt fra forrige frame
    vindu.fill("white")
    
    # Hendelser
    for hendelse in pygame.event.get():
        # pygame.QUIT hendelsen skjer når brukeren klikker på X for å lukke vinduet
        if hendelse.type == pygame.QUIT:
            kjorer = False
 
 
    # Input fra tastatur:
    taster = pygame.key.get_pressed()
    spillebrett.spiller_input(taster)
 

    # Input fra mus:
    mus_posisjon = pygame.mouse.get_pos()
    mus_klikk = pygame.mouse.get_pressed()
    menybrett.aktiver_spill(mus_posisjon, mus_klikk, taster)
 
    # Oppdater spill her:
    if menybrett.spill_aktiv == True:
        spillebrett.flytt_hinder(HOYDE)
        spillebrett.aktiver_ball(HOYDE, BREDDE)
        spillebrett.aktiver_boosters()

        spillebrett.tid_siden_forrige_nye_ball += 1
        spillebrett.tid_mellom_booster += 1


    # Tegn på skjermen her: spiller kun når du har trykket på startknappen.
    # Startknappen endrer spilltilstanden
    if menybrett.spill_aktiv == True:
        spillebrett.tegn(vindu)
    else:
        menybrett.tegn(vindu)

 
    # flip() oppdater vinduet med alle endringer
    pygame.display.flip()
 
    # klokke.tick(60) begrenser spillet til 60 FPS (frames per second)
    klokke.tick(60) 
 
pygame.quit()