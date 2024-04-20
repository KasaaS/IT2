import pygame

class Spillobjekt:
    def __init__(self, farge: str):

        self.surface = pygame.Surface((50, 50)) # Definerer størrelsen, 50px bredt 50px høyt
        self.rect = self.surface.get_rect() # Lager rektangel rundt surface til objektet
        self.surface.fill(farge)


    def plassering(self, x: int, y: int):
        # Setter spillobjektet i kordinate x,y. Kan bare gjøres når vi har en rect
        self.rect.center = (x,y)

    # dx = delta x, endring i x.
    def flytt(self, dx: int, dy: int):

        # move_ip = move in place. Denne vi bør bruke.
        self.rect.move_ip(dx, dy)

    def tegn(self, surface: pygame.Surface):
        surface.blit(self.surface, self.rect)