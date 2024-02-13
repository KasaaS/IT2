import pygame, random
from os import system

system("clear")


# Klasser
class Matbit:
    def __init__(self):
        self.bilde = pygame.image.load("bilder2/plank.png").convert_alpha()
        self.bilde = pygame.transform.scale_by(self.bilde, 0.08)
        self.ramme = self.bilde.get_rect()
        self.ramme.centerx = random.randint(0, BREDDE)
        self.ramme.centery = random.randint(0, HOYDE)

    def tegn(self, vindu):
        vindu.blit(self.bilde, self.ramme)


class Celle:
    def __init__(self, navn: str, radius: int, bildesti: str, x: int, y: int, farge: str):
        self.navn = navn
        self.radius = radius
        self.bilde_original = pygame.image.load(bildesti).convert_alpha()
        self.bilde = pygame.transform.scale(self.bilde_original, (self.radius*2, self.radius*2))
        self.ramme = self.bilde.get_rect()
        self.ramme.centerx = x
        self.ramme.centery = y
        self.farge = farge

    def beveg(self, mus_x: int, mus_y: int):
        # self.ramme.centerx = mus_x
        # self.ramme.centery = mus_y

        if mus_x > self.ramme.centerx:
            self.ramme.centerx += 1
        elif mus_x < self.ramme.centerx:
            self.ramme.centerx -= 1

        if mus_y > self.ramme.centery:
            self.ramme.centery += 1
        elif mus_y < self.ramme.centery:
            self.ramme.centery -= 1
    
    def spis(self, motspiller=None):

        if motspiller:
            self.radius += motspiller.radius
        else:
            self.radius += 1

        self.oppdater_bilde()

    def bli_spist(self):
        self.radius = 10
        self.oppdater_bilde()
        
    def oppdater_bilde(self):
        self.bilde = pygame.transform.scale(self.bilde_original, (self.radius*2, self.radius*2))
        gammel_x = self.ramme.centerx
        gammel_y = self.ramme.centery
        self.ramme = self.bilde.get_rect()
        self.ramme.centerx = gammel_x
        self.ramme.centery = gammel_y


    def tegn(self, vindu):
        pygame.draw.circle(vindu, self.farge, (self.ramme.centerx, self.ramme.centery), self.radius + 4)
        vindu.blit(self.bilde, self.ramme)
    



# 1. Oppsett
pygame.init()
BREDDE = 800
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE,HOYDE))
klokke = pygame.time.Clock()  


pl2 = Celle("Johnny", 50, "bilder2/pl2.png", 100, 200, "green")


motspillere = [
    Celle("Ed", 25, "bilder2/pl1.png", 500, 400, "red"),
    Celle("Ed", 50, "bilder2/pl1.png", 50, 120, "red"),
    Celle("Ed", 50, "bilder2/pl1.png", 310, 520, "red")
]


matbiter = []
for _ in range(10):
    matbiter.append(Matbit())




while True:

    # 2. Håndter input
    for hendelse in pygame.event.get():

        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    
    mus_x, mus_y = pygame.mouse.get_pos()



    # 3. Oppdater spill
    pl2.beveg(mus_x, mus_y)

    for i in range(len(matbiter) -1, -1, -1):
        if pl2.ramme.colliderect(matbiter[i].ramme):
            pl2.spis()
            matbiter.pop(i)

    for i in range(len(motspillere) -1, -1, -1):
        if pl2.ramme.colliderect(motspillere[i].ramme):
            if pl2.radius > motspillere[i].radius:
                pl2.spis(motspillere[i])
                motspillere.pop(i)

            elif pl2.radius < motspillere[i].radius:
                pl2.bli_spist()



    # 4. Tegn
    vindu.fill("white")
    pl2.tegn(vindu)

    for motspiller in motspillere:
        motspiller.tegn(vindu)

    for matbit in matbiter:
        matbit.tegn(vindu)
    

    pygame.display.flip()
    klokke.tick(FPS)