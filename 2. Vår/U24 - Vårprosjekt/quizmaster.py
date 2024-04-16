import pygame
from figur import Figur

class Quizmaster(Figur):
    def __init__(self, bildesti: str, størrelse: int, vindu_bredde: int, vindu_hoyde: int):
        super().__init__(bildesti, størrelse)


        self.ramme.centerx = vindu_bredde / 2       # Setter spilleren i startposisjon
        self.ramme.centery = vindu_hoyde / 2 

        self.navn = "Quizmaster"



