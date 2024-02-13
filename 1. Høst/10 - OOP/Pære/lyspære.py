# lyspære

class Lyspære():
    def __init__(self):
        self._på = False

    def tenn(self):
        self._på = True
    
    def slukk(self):
        self._på = False

    def er_på(self):
        return self._på


# linja under gjør at testkoden kun kjøres i denne filen.
if __name__ == "__main__":
    min_pære = Lyspære()
    stue_pære = Lyspære()
    soverom_pære = Lyspære()
    # print pæra i stua er på
    stue_pære.tenn()

    if stue_pære.er_på():
        print("pæra i stua er på!")

            