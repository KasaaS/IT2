from oppgave4_2 import Sang


class Spilleliste():
    def __init__(self, navn: str):
        
        self.navn = navn
        self.sanger = []



    def legg_til_sang(self, sang):
        self.sanger.append(sang)

    

    def lengde(self):
        antall_sanger = 0
        for sang in self.sanger:
            antall_sanger += 1
        return antall_sanger
    


    def spill_alle(self):
        for sang in self.sanger:
            sang.spill()

    

    def tittel_i_liste(self, tittel: str):
        for sang in self.sanger:
            if tittel == sang.tittel:
                return True
        return False
        

    
    def artistliste(self, artist: str):
        artistliste = []
        for sang in self.sanger:
            if artist == sang.artist:
                artistliste.append(sang)

        return artistliste





if __name__ == "__main__":
    min_liste = Spilleliste("Min Liste")
    sang1 = Sang("Oslo vet, Pt.2","Evig Ferie")
    sang2 = Sang("The Weeknd", "Blinding Lights")
    sang3 = Sang("The Weeknd", "Your Eyes")
    sang4 = Sang("The Weeknd", "The Hills")
    sang5 = Sang("Cezinando", "Kristoffer Robin",)


    min_liste.legg_til_sang(sang1)
    min_liste.legg_til_sang(sang2)
    min_liste.legg_til_sang(sang3)
    min_liste.legg_til_sang(sang4)
    min_liste.legg_til_sang(sang5)


    print(min_liste.sanger)
    print(min_liste.lengde())


    min_liste.spill_alle()


    print(min_liste.sanger)
    print(min_liste.tittel_i_liste("Blinding Lights"))
    print(min_liste.tittel_i_liste("Kristoffer Robin"))
    print(min_liste.tittel_i_liste("Evig Ferie"))


    print(min_liste.artistliste("The Weeknd"))