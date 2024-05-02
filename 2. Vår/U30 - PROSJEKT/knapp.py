from figur import Figur

class Knapp(Figur):
    def __init__(self, x: int, y: int, hoyde: int, bredde: int) -> None:
        super().__init__(x, y, bredde, hoyde, "orange")