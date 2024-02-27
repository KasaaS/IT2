from politiker import Politiker

class Fantasiparti:
    def __init__(self, navn: str, eier: str): # Metode som kjører når et parti opprettes 
        self.navn: str = navn
        self.eier: str = eier
        self.poeng = 0
        self.saldo = 100_000
        self.partileder: Politiker = None
        self.politikere: list[Politiker] = []

    def __str__(self): # Metode som bestemmer hvordan print skal se ut.
        return f"{self.navn} - {self.eier} ({self.poeng} poeng, {self.saldo} kr)"

    
    def kjøp_politiker(self, politiker: Politiker):

        if self.saldo >= politiker.verdi and politiker not in self.politikere:
            self.saldo -= politiker.verdi
            self.politikere.append(Politiker)
        else:
            print("Avvist")


    def self_politiker(self, politiker: Politiker):

        if politiker in self.politikere:
            self.politikere.remove(politiker)
            self.saldo += politiker.verdi
        else:
            ("Politiker ikke med i partiet")

    def vis_parti(self):
        print(f"-- {self.navn} --")
        print(f"Poeng: {self.poeng}")
        print(f"Saldo: {self.saldo}")
        print(f"Medlemmer:")
        for politiker in self.politikere:
            print(politiker)
        print()



if __name__ == "__main__":
    print("Tester Fantasiparti")
    testparti = Fantasiparti("Apolitisk testparti", "Test")
    testparti2 = Fantasiparti("Parti2", "Parti2 Sjef")
    print(testparti)
    print(testparti2)