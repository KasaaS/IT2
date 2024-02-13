class Lag():
    def __init__(self, navn: str, ):
        self.navn = navn
        self.spillere = []
        self._seier = 0
        self._uavgjort = 0
        self._tap = 0



    def hent_navn(self):
        return self.navn

    def hent_poeng(self):
        self.poeng = self._seier*3 + self._uavgjort*1 + self._tap*0
        return self.poeng

    def legg_til_spiller(self, spiller):
        self.spillere.append(spiller)
        

    def spill_kamp(self):
        for spiller in self.spillere:
            spiller.spill_kamp()

    def seier(self):
        self._seier += 1
        self.spill_kamp()

    def uavgjort(self):
        self._uavgjort += 1
        self.spill_kamp()

    def tap(self):
        self._tap += 1
        self.spill_kamp()

    def finn_spiller(self, navn):
        for spiller in self.spillere:
            if spiller.sjekk_navn(navn):
                return spiller
        return None