## Oppgave 3-1
def er_primtall(tall):
    for i in range(tall):
        if tall % i == 0:
            return True
    return False


## Oppgave 3-2

# Definerer funksjonen og tar inn tall som variabel.
def er_primtall(tall: int):
    """ 
    En funksjon som sjekker primtall

    Atributter
        tall (int) = tallet du vil sjekke
    """

    # sjekker hver i som er mindre enn tall
    for i in range(tall):

        # sjekker om tall delt på i = 0
        if tall % i == 0:

            # om stemmer, returnerer true
            return True

    # om ikke stemmer returnerer false.
    return False