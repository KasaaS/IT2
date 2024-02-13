from lyspære import Lyspære

class Rom:
    def __init__(self):
        self._pærer: list[Lyspære] = []

    def legg_til_pære(self, pære):
        self._pærer.append(pære)

    def skru_på_lys(self):
        for pære in self._pærer:
            pære.tenn()

    def skru_av_lys(self):
        for pære in self._pærer:
            pære.slukk()

    def __str__(self):
        return f"Rom: {len(self._pærer)}"



if __name__ == "__main__":
    print("Tester rom.py")

    # opprett et rom
    stue = Rom()

    # oppretter 3 pærer
    for i in range(3):
        stue.legg_til_pære(Lyspære())


    stue.skru_på_lys()
    print(stue)


