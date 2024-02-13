import pygame

class Planet:
    def __init__(self, x, y, radius, bilde):    # Kan bruke verdiene satt i klassen som variabler
        self.x = x                              # I Edd kunne jeg laget klasse planke og brukt det for alle plankene
        self.y = y
        self.radius = radius
        self.surface = pygame.image.load(bilde)
        self.surface = pygame.transform.scale(self.surface, ( 2 * self.radius, 2 * self.radius))
    
    def tegn(self, vindu):
       # pygame.draw.circle(vindu, "red", (self.x,self.y), self.radius)
       vindu.blit(self.surface, (self.x, self.y))