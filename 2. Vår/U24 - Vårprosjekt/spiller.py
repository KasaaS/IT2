import pygame
from figur import Figur

class Spiller(Figur):
    def __init__(self, bildesti: str, størrelse: int):
        super().__init__(bildesti, størrelse)


        self.ramme.centerx = 393     # Setter spilleren i startposisjon
        self.ramme.bottom = 435

        self.ramme_collide = self.bilde.get_rect()
        self.ramme_collide.height = self.ramme_collide.height/2
        self.ramme_collide.bottom = self.ramme.bottom

        self.liv = 3


        
    def flytt(self, dx: int, dy: int):

        self.ramme.x += dx
        self.ramme.y += dy



    def mist_liv(self):
            self.liv -= 1