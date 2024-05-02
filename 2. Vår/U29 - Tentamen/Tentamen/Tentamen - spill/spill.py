import pygame
import pygame.freetype

from spiller import Spiller
from hinder import Hinder
from ball import Ball

 
# Oppsett av pygame
pygame.init()
BREDDE = 800 # bredde på vinduet
HOYDE = 600  # høyde på vinduet
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
kjorer = True

poeng_font = pygame.freetype.SysFont("Arial", 50)
 
spiller1 = Spiller(100, HOYDE/2)
spiller2 = Spiller(700, HOYDE/2)


hinder_y = 100
hindere = []
for i in range(3):
    hindere.append(Hinder(400, hinder_y))
    hinder_y += 150


baller = []
ball = Ball(400,300)
baller.append(ball)



# OPPSETT AV SPILL HER:
 
while kjorer:
    # fyll skjermen med en farge for å fjerne alt fra forrige frame
    vindu.fill("black")
    
    # Hendelser
    for hendelse in pygame.event.get():
        # pygame.QUIT hendelsen skjer når brukeren klikke på X for å lukke vinduet
        if hendelse.type == pygame.QUIT:
            kjorer = False
 
 
    # Input fra tastatur:
    taster = pygame.key.get_pressed()
    if taster[pygame.K_UP]:
        spiller2.retning = -1
    if taster[pygame.K_DOWN]:
        spiller2.retning = 1
    if taster[pygame.K_w]:
        spiller1.retning = -1
    if taster[pygame.K_s]:
        spiller1.retning = 1



    # Oppdater spill:
    spiller1.oppdater_posisjon()
    spiller2.oppdater_posisjon()
    for ball in baller:
        ball.oppdater_posisjon()


    if spiller1.rect.colliderect(ball.rect) or spiller2.rect.colliderect(ball.rect):
        ball.skift_retning()

    for hinder in hindere:
        if hinder.rect.colliderect(ball.rect):
            ball.skift_retning()
    
    if ball.rect.left == 0:
        spiller2.poeng +=1 
        for ball in baller:
            ball.reset_ball()
    if ball.rect.right == 800:
        spiller1.poeng +=1 
        for ball in baller:
            ball.reset_ball()
    
 
    # Tegn på skjermen her:
    spiller1.tegn(vindu)
    spiller2.tegn(vindu)
    for hinder in hindere:
        hinder.tegn(vindu)

    poeng_font.render_to(vindu, (10, 10), str(spiller1.poeng), "white")
    poeng_font.render_to(vindu, (765, 10),str(spiller2.poeng), "white")

    for ball in baller:
        ball.tegn(vindu)
    
    # flip() oppdater vinduet med alle endringer
    pygame.display.flip()
 
    # klokke.tick(60) begrenser spillet til 60 FPS (frames per second)
    klokke.tick(60) 
 
pygame.quit()