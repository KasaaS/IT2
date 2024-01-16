# Algoritme 1: Høyeste tall

def høyeste(liste: list[int]):
    høyest = liste[0]
    for tall in liste:
        if tall > høyest:
            høyest = tall
    return høyest
   
min_liste = [2,6,-10,100,95]
print(høyeste(min_liste))

# python funksjon for høyeste og minste tall i lister.
print(max(min_liste))
print(min(min_liste))



# Algoritme 2: Gjennomsnitt

def gjennomsnitt(liste: list[int]):
    total = 0
    antall = 0

    for tall in liste:
        total += tall
        antall += 1
    
    return total / antall

print(gjennomsnitt(min_liste))



# Algoritme 3: nest høyest

def nest_høyest(liste: list[int]):
    høyest = -9999
    nest_høyest = -9999

    for tall in liste:
        if tall > høyest:
            nest_høyest = høyest
            høyest = tall
        elif tall > nest_høyest:
            nest_høyest = tall
    return nest_høyest

print(nest_høyest(min_liste))



# Algoritme 4.1: n_høyeste

def n_høyeste(liste: list[int], n: int):
    høyeste_n = []
    for i in range(0,n):
        høyest = høyeste(liste)
        liste.remove(høyest)
        høyeste_n.append(høyest)
    return høyeste_n

print(n_høyeste([2,6,-10,100,95],3))


def n_høyeste_alt(liste:list[int], n: int):
    sortert = sorted(liste, reverse=True)
    return sortert[:n]
print(n_høyeste_alt([2,6,-10,100,95], 3))

# Algoritme 4.2: 
