
def fjern_vokaler(setning, vokaler):
    kopi = ""
    for bokstav in setning:
        if bokstav not in vokaler:
            kopi += bokstav
            
    return kopi


print(fjern_vokaler("ha det fint", ["a", "e", "i", "o", "u"]))