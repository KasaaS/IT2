import pygame
import random

class Ball():
    def __init__(self, vindu_bredde: int):
        self.bilde = pygame.image.load("bilder/ball.png").convert_alpha()
        self.ramme = self.bilde.get_rect()


        # Flytter ballen til start
        self.ramme.centerx = random.randint(0, vindu_bredde)
        self.ramme.top = 0

    
    def fall(self, vindu_høyde: int, vindu_bredde: int):
        if self.ramme.top > vindu_høyde:
            self.ramme.y = 0
            self.ramme.x = random.randint(0, vindu_bredde)


        self.ramme.y += 1

    
    def tegn(self, vindu: pygame.Surface):
        vindu.blit(self.bilde, self.ramme)


