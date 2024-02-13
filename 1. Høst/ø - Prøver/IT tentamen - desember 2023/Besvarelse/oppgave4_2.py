class Sang():
    def __init__(self, artist: str, tittel: str):

        self.tittel = tittel
        self.artist = artist
        self.avspillinger = 0



    def spill(self):
        self.avspillinger += 1
        print(f"Spiller {self.tittel}, - {self.avspillinger}, avspillinger")



    def sjekk_tittel(self, tittel):
        if self.tittel == tittel:
            return True
        else:
            return False
        


    def sjekk_artist(self, artist):
        if self.artist == artist:
            return True
        else:
            return False


    def __repr__(self):
        return f"{self.artist}, {self.tittel}"

    


if __name__ == "__main__":
    sang = Sang("Evig Ferie", "Oslo vet, Pt.2")

    sang.spill()


    print(sang.sjekk_tittel("Oslo vet, Pt.2"))
    print(sang.sjekk_tittel("Kristoffer robin"))


    print(sang.sjekk_artist("Evig Ferie"))
    print(sang.sjekk_artist("Cezinando"))

