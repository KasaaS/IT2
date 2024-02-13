from os import system
system("clear")

runde = 0

spill = []
spiller1 = []
spiller2 = []

def mest_vanlig(list):
    return max(set(list), key=list.count)

def beregn_score(valg1, valg2):
    if valg1 == valg2:
        if valg1 == "svik":
            return [1 , 1]
        else:
            return [3 , 3]
    elif valg1 == "svik":
        return [5 , 0]
    else:
        return [0, 5]



def spill_snilt(tidligere_spill):
    for liste in tidligere_spill:
        spiller2.append(liste[1])
    if mest_vanlig(spiller2) == 5 or mest_vanlig(spiller2) == 1:
        return "svik"
    else:
        return "samarbeid"

def spill_slemt(tidligere_spill):
    for liste in tidligere_spill:
        spiller2.append(liste[1])

    if runde <= 5:
        return "samarbeid"
    else:
        return "svik"


curr_spill = beregn_score("samarbeid" , "svik")

for i in range(10):
    runde += 1
    spill.append(curr_spill)
    curr_spill = beregn_score(spill_snilt(spill) , "samarbeid")

print(spill)