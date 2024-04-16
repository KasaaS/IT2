from spillobjekt import Spillobjekt
from sau import Sau


# For å arve ta inn spillobjekt
class Menneske(Spillobjekt):
    def __init__(self):
        super().__init__()

        self.fart:int
        self.poeng:int
        # bool = True/False
        self.baererSau: bool



    def beveg(self):
        pass

    def reduser_fart(self, endring: int):
        pass
    
    def ok_poeng(self, poeng: int):
        self.poeng += 1

    def baer_sau(self, sau: Sau):
        pass

    def sjekk_kollisjon(self):
        pass