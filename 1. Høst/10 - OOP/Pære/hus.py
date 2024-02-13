from rom import Rom


class Hus():
    def __init__(self) -> None:
        self._rom: list[Rom] = []


    def legg_til_rom(self, rom: Rom):
        self._rom.append(rom)

    def skru_av_strøm(self):
        for rom in self._rom:
            rom.skru_av_lys()

if __name__ == "__main__":
    thors_hus = Hus()
    thors_hus.legg_til_rom(Rom())
    
