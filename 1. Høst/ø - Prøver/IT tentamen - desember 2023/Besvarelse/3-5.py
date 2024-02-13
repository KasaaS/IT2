# kode til oppgave 3-1
def per_stream(land):
    Ordbok =  {"Norge": 0.55,
     "Sverige": 0.44,
     "Finland": 0.44,
     "Danmark": 0.52,
     "Island": 0.62}
    
    if land in Ordbok:
        return Ordbok[land]
    else:
        return 0.24
    

# kode til oppgave 3-2
def andel_til_artist(antall_streams):
    if antall_streams <= 399999:
        return 0
    elif antall_streams <= 29999999:
        return 0.4
    else:
        return 0.7
    

# kode til oppgave 3-3
def penger_tjent(antall_streams, land):
    return andel_til_artist(antall_streams)*per_stream(land)* antall_streams


# kode til oppgave 3-4
def populære(artistliste):
    populærliste = []

    for artist in artistliste:
        if artist[1] > 100000000:
            populærliste.append(artist)

    return populærliste



def royalties(artistliste):
    penge_per_artist = []

    for artist in artistliste:
        antall_streams = artist[2]
        land = artist[1]
        penge_per_artist.append([artist[0],int(penger_tjent(antall_streams,land))])

    return penge_per_artist
    

artistliste = [
    ["Sigur Ros", "Island", 1047010],
    ["Emma Steinbakken", "Norge", 3459239]
]

print(royalties(artistliste))