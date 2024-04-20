from spillobjekt import Spillobjekt


# For å arve ta inn spillobjekt
class Menneske(Spillobjekt):
    def __init__(self):
        super().__init__("green") # Må sette inn fargen vi tar inn fra spillobjekt. Sender den videre til spillobjekt

        self.fart_x:int = 0
        self.fart_y:int = 0
        self.poeng:int = 0
        # bool = True/False
        self.baerer_sau: bool = False
        # Bruker metoden plassering fra spillobjekt
        self.plassering(75, 300)



    def beveg(self):
        if self.baerer_sau:
            self.flytt(self.fart_x*0.8, self.fart_y*0.8)
        else:
            self.flytt(self.fart_x, self.fart_y)