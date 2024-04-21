import pygame
from spillobjekt import Spillobjekt
from menneske import Menneske
from sau import Sau
from hindring import Hindring

# Starter med spillbrett da den er relevant for spillobjekt.

class Spillebrett:
    def __init__(self, hoyde, bredde):

        self.hoyde: int = hoyde
        self.bredde: int = bredde
        self.objekter: list[Spillobjekt] = []

        # Må opprette et surface for å så tegne brettet. 
        # Alle ting i pygame må ha surface og rect.
        self.surface = pygame.Surface( (self.bredde, self.hoyde) )
        self.rect = self.surface.get_rect()

        # Plasserer rektangelet til brettet i (x,y) av vinduet.
        self.rect.topleft = (0,0)
        self.surface.fill("white")

        

        # Oppretter en spiller som et menneske
        self.spiller1 = Menneske()
        # Oppretter tre sauer og putter dem alle i listen sauer.
        self.sauer: list[Sau] = []
        for i in range(3):
            self.sauer.append(Sau())

        self.hindringer: list[Hindring] = []
        for i in range(3):
            self.hindringer.append(Hindring())






    def legg_til_objekt(self, nytt_objekt: Spillobjekt):
        #Legger til nytt objekt i objektlisten
        self.objekter.append(nytt_objekt)



    def fjern_objekt(self, objekt: Spillobjekt):
        # Fjerner objekt
        self.objekter.remove(objekt)

    

    def tegn(self, vindu: pygame.Surface):
        # Tegner spillobjekter før vi tegner vinduet for hele brettet. Tegner spilleren på overflaten til spillbrettet.
        self.spiller1.tegn(self.surface)

        # Tegner sauer som er satt i en liste. Vi bruker midlertidige variabler i for løkker.
        for sau in self.sauer:
            sau.tegn(self.surface)

        for hindring in self.hindringer:
            hindring.tegn(self.surface)
    
        # Tegner spillbrettets surface i posisjonen til spillbrettets rect på vinduet.
        vindu.blit(self.surface, self.rect)