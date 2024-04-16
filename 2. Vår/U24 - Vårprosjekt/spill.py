import pygame
from spiller import Spiller
from quizmaster import Quizmaster
from quiz import Quiz



# 1. Oppsett
pygame.init()
BREDDE = 600
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE,HOYDE))
klokke = pygame.time.Clock()

pygame.display.set_caption("Planke")
font = pygame.font.SysFont("Arial", 32) # Skrifttype


spiller = Spiller("bilder/spiller.png", 0.1, 5, BREDDE, HOYDE)
 
 
while True:

    # 2. Håndter input

    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
        if hendelse.type == pygame.KEYDOWN:
            if hendelse.key == pygame.K_LEFT or hendelse.key== pygame.K_a:
                spiller.flytt(-1, 0)
            if hendelse.key == pygame.K_RIGHT or hendelse.key== pygame.K_d:
                spiller.flytt(1, 0)
            if hendelse.key == pygame.K_UP or hendelse.key== pygame.K_w:
                spiller.flytt(0, -1)
            if hendelse.key == pygame.K_DOWN or hendelse.key== pygame.K_s:
                spiller.flytt(0, 1)


    # 3. Oppdater spill




    # 4. Tegn

        spiller.tegn(vindu)  

        pygame.display.flip()
        klokke.tick(FPS)