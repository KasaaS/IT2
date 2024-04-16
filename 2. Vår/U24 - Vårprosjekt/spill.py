import pygame
from spiller import Spiller
from quizmaster import Quizmaster
from svar import Svar


# 1. Oppsett
pygame.init()
BREDDE = 600
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE,HOYDE))
klokke = pygame.time.Clock()

pygame.display.set_caption("SJUK QUIZ!")
font = pygame.font.SysFont("Arial", 32) # Skrifttype


collide_tilstand = "false"
svar_tilstand = "false"


spiller = Spiller("bilder/planke.png", .15)
quizmaster = Quizmaster("bilder/quizmaster.png", .2, BREDDE, HOYDE)

svar_ja = Svar("ja", font, 200, 350)
svar_nei = Svar("nei", font, 400, 350)



 
while True:

    # 2. Håndter input

    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        spiller.flytt(-2, 0)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        spiller.flytt(2, 0)
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        spiller.flytt(0, -2)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        spiller.flytt(0, 2)


    # 3. Oppdater spill               



    # 4. Tegn
    vindu.fill("green")


    # Selv om dette er input, tegning og oppdatering av spill, må jeg ha den her for at den skal fungere.

    if collide_tilstand == "false":
        if spiller.ramme.colliderect(quizmaster.ramme):
            collideskrift = font.render("Quizmaster - (E)", True, "black")
            vindu.blit(collideskrift,(BREDDE/3,HOYDE/11))

        if keys[pygame.K_e]:
            collide_tilstand = "true"

    if collide_tilstand == "true":
        collideskrift = font.render("avslutt spill?", True, "black")
        vindu.blit(collideskrift,(BREDDE/3,HOYDE/11))

        svar_ja.tegn(vindu,200, 350)
        svar_nei.tegn(vindu,400, 350)


    if spiller.ramme.colliderect(svar_ja.ramme):
        svar_ja.svar_funksjon()

    if spiller.ramme.colliderect(svar_nei.ramme):
        svar_tilstand = "true"



    if svar_tilstand == "true":
        svar_nei_oppgave = font.render("GÅ PÅ JA!", True, "black")
        vindu.blit(svar_nei_oppgave,(BREDDE/3,HOYDE/6))





    spiller.tegn(vindu) 
    quizmaster.tegn(vindu)

    pygame.display.flip()
    klokke.tick(FPS)