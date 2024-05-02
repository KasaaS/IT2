import random
from figur import Figur

class Ball(Figur):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y , "white", 10, 10)
        self.xfart = random.randint(-1,1)
        self.yfart = random.randint(-1,1)

        if self.xfart == 0:
            self.xfart = random.randint(-1,1)
        if self.yfart == 0:
            self.yfart = random.randint(-1,1)

        
    def oppdater_posisjon(self):
        if self.rect.bottom > 600:
            self.yfart = -1
        elif self.rect.top < 0:
            self.yfart = 1

        self.rect.y += self.yfart
        self.rect.x += self.xfart

    
    def skift_retning(self):
        self.xfart *= -1
        self.yfart *= random.randint(-1,1)

    def reset_ball(self):
        self.rect.centerx = 400
        self.rect.centery = 300