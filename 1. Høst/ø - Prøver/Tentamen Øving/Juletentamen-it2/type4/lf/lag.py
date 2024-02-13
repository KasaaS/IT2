from spiller import Spiller
class Lag():
    def __init__(self) -> None:
        self.spillere = []
    
    def legg_til_spiller(self, spiller):
        self.spillere.append(spiller)

    def spill_kamp(self):
        for spiller in self.spillere:
            spiller.spill_kamp()

if __name__ == "__name__":
    norge = Lag()
    norge.legg_til_spiller(Spiller("Caroline"))
    norge.legg_til_spiller(Spiller("Ada"))
    norge.spill_kamp()
