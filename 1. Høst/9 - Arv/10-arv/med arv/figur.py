import pygame
import random


class Figur():
    def __init__(self, bildesti: str, ):
        self.bilde = pygame.image.load(bildesti).convert_alpha()
        self.ramme = self.bilde.get_rect()

    
    def tegn(self, vindu: pygame.Surface):
        vindu.blit(self.bilde, self.ramme)


    def fall(self, vindu_høyde: int, vindu_bredde: int):
        if self.ramme.top > vindu_høyde:
            self.ramme.y = 0
            self.ramme.x = random.randint(0, vindu_bredde)
        self.ramme.y += 1