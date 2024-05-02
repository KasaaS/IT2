from figur import Figur

class Spiller(Figur):
    def __init__(self, x:int, y:int):
        super().__init__(x, y, "white", 150, 20)
        self.fart = 1
        self.retning = 0
        self.poeng = 0

    def oppdater_posisjon(self):
        self.rect.y += self.fart * self.retning

from figur import Figur
