

class Pokemon():
    def __init__(self,number: int, name: str, type_1: str, type_2: str, total: int, hp: int, attack: int, defense: int, sp_atk: int, sp_def: int, speed: int, generation: int, legendary):

        self.number = number
        self.name = name
        self.type_1 = type_1
        self.type_2 = type_2
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed
        self.generation = generation
        self.legendary = legendary


    def __str__(self) -> str:
        return f"{self.name} ({self.hp})"
    
    def angrip(self, motstander):
        ny_hp = self.attack - motstander.defense
        if ny_hp < 0:
            motstander.hp = 0
        else:
            motstander.hp -= self.attack - motstander.defense



if __name__ == "__main__":
    charizard = Pokemon(6,"Charizard", "Fire", "Flying", 534, 78, 84, 78, 109, 85, 100, 1, False)
    bulba = Pokemon(1,"Bulbasaur","Grass","Poison",318,45,49,49,65,65,45,1,False)

    print(charizard)
    print(bulba)
    charizard.bli_angrepet(bulba)
    print(charizard)
    print(bulba)