import pygame
from spillobjekt import Spillobjekt

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



    def legg_til_objekt(self, nytt_objekt: Spillobjekt):
        #Legger til nytt objekt i objektlisten
        self.objekter.append(nytt_objekt)

    def fjern_objekt(self, objekt: Spillobjekt):
        # Fjerner objekt
        self.objekter.remove(objekt)

    
    def tegn(self, vindu: pygame.Surface):
        # Tegner spillbrettets surface i posisjonen til spillbrettets rect på vinduet.
        vindu.blit(self.surface, self.rect)