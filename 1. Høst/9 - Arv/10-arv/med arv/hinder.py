from figur import Figur
import random

class Hinder(Figur):
    def __init__(self, vindu_bredde: int):
        super().__init__("bilder/ball.png")


        # Flytter ballen til start
        self.ramme.left = random.randint(0, vindu_bredde - self.ramme.width)
        self.ramme.top = 0

    
    def fall(self, vindu_høyde: int, vindu_bredde: int):
        if self.ramme.top > vindu_høyde:
            self.ramme.y = 0
            self.ramme.x = random.randint(0, vindu_bredde)
        self.ramme.y += 1


