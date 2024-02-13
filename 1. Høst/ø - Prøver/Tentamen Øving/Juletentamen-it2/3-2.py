
def pris_ink_frakt(varepris):
    if varepris > 1000:
        return varepris
    elif varepris >= 500 or varepris >= 1000:
        return varepris + 50
    else:
        return varepris + 80
    

print(pris_ink_frakt(1300))