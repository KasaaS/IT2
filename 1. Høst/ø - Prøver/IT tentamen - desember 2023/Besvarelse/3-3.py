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
    




# Ny kode til oppgave 3-3
def andel_til_artist(antall_streams):
    if antall_streams <= 399999:
        return 0
    elif antall_streams <= 29999999:
        return 0.4
    else:
        return 0.7
    


def penger_tjent(antall_streams, land):
    return int(andel_til_artist(antall_streams)*per_stream(land)* antall_streams)


print(penger_tjent(5000000,"Norge"))
print(penger_tjent(100000000,"Island"))
