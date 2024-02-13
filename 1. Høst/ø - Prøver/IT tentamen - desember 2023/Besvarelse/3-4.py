def populære(artistliste):
    populærliste = []

    for artist in artistliste:
        if artist[1] > 100000000:
            populærliste.append(artist)

    return populærliste



artistliste = [
    ["Taylor swift", 109940000],
    ["The Weeknd", 105410000],
    ["Justin Bieber", 83820000],
    ["Drake", 81980000],
    ["Ariana Grande", 81800000],
]

print(populære(artistliste))