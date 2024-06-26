import pygame

from figur import Figur
from knapp import Knapp


class Meny(Figur):
    def __init__(self, hoyde, bredde):
        super().__init__(bredde/2, hoyde/2, bredde, hoyde, "orange")

        self.hoyde: int = hoyde
        self.bredde: int = bredde
        self.objekter: list[Figur] = []

        # definerer en font
        self.font = pygame.font.SysFont("Arial", 50)
        self.spillknapp = Knapp(bredde/2, 400, 50, 300)


    def aktiver_spill(self, mus_posisjon, mus_klikk, taster):
        if mus_klikk[0]:
            if mus_posisjon[0] > self.spillknapp.rect.left and mus_posisjon[0] < self.spillknapp.rect.right:
                if mus_posisjon[1] > self.spillknapp.rect.top and mus_posisjon[1] < self.spillknapp.rect.bottom:
                    self.spill_aktiv = True
        elif taster[pygame.K_RETURN]:
            self.spill_aktiv = True


    def tegn(self, vindu: pygame.Surface):
        self.surface.fill("black")
        # Tegner spillobjekter før vi tegner vinduet for hele brettet. Tegner spilleren på overflaten til spillbrettet.

        # Tegner spillbrettets surface i posisjonen til spillbrettets rect på vinduet.
        startskrift = self.font.render("Hjemmelaga PinPong!", True, "white")
        self.surface.blit(startskrift, (self.bredde/4 - 50, self.hoyde/2))

        self.spillknapp.tegn(self.surface)
        vindu.blit(self.surface, self.rect)