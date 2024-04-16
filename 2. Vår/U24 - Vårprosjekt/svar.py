import pygame
from figur import Figur


class Svar():
    def __init__(self, svar:str, font, x, y):

        self.svar = svar

        self.tittel = font.render(str(svar), True, "black")
        self.ramme = self.tittel.get_rect()
    
        self.ramme.x = x
        self.ramme.y = y


    def tegn(self, vindu: pygame.Surface, x, y):
        pygame.draw.rect(vindu, (255,255,255), self.ramme, 2)
        vindu.blit(self.tittel,(x,y))


    def svar_funksjon(self):
        if self.svar == "ja":
            raise SystemExit
        
