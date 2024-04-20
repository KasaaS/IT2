import random
from spillobjekt import Spillobjekt


class Hindring(Spillobjekt):
    def __init__(self):
        super().__init__("red")


        # lager en tilfeldig y og setter den i plassering. 
        tilfeldig_y = random.randint(50, 550) # Variabler uten self. glemmes når init metoden er ferdig.
        tilfeldig_x = random.randint(150,600)
        self.plassering(tilfeldig_x, tilfeldig_y)