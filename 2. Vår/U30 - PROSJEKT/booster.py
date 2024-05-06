import random

from figur import Figur


class Booster(Figur):
    def __init__(self, x: int, y: int, hoyde: int, bredde: int) -> None:
        super().__init__(x, y, bredde, hoyde, "green")


    def tilfedlig_boost(self):
        tilfeldig_tall = random.randint(1,1)

        if tilfeldig_tall == 0:
            return "MINK_FART"
        if tilfeldig_tall == 1:
            return "ØK_FART"
