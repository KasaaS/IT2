import pygame
from fotballspiller import Fotballspiller
from ball import Ball


# 1. Oppsett
pygame.init()
BREDDE = 600
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

spiller = Fotballspiller(BREDDE, HOYDE)
ball = Ball(BREDDE)


while True:
    # 2. Håndter input
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    taster = pygame.key.get_pressed()
    if taster[pygame.K_LEFT]:
        spiller.flytt(-1)
    if taster[pygame.K_RIGHT]:
        spiller.flytt(1)

        
    # 3. Oppdater spill
    ball.fall(HOYDE, BREDDE)

    # 4. Tegn
    vindu.fill("white")
    spiller.tegn(vindu)
    ball.tegn(vindu)

    pygame.display.flip()
    klokke.tick(FPS)