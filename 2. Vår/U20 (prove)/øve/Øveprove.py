import json
with open("stortinget.json", encoding="utf-8") as fil:
    data = json.load(fil)
 
politikere = data["representanter_liste"]
 
# 1. Lag en for-løkke som printer navn og tilhørnde parti på alle politikerne

for politiker in politikere:
    print(f"{politiker['fornavn']} {politiker['etternavn']}: {politiker['parti']['navn']}")
 


# 2. Lag en ordbok som teller antall representanter hvert parti har
antall = {}

for politiker in politikere:
    parti = politiker['parti']['navn']
    if parti not in antall:
        antall[parti] = 1
    else:
        antall[parti] += 1
print(antall)


        
# 3. Hvilket parti har flest representanter på Stortinget og hvor mange har de?
# Tips: https://it2.thorcc.no/databehandling-og-algoritmer/lokker-lister-og-ordboker#sortering-av-ordbøker-med-verdier

antall_liste = list(antall.items())
antall_sortert = sorted(antall_liste, key=lambda parti: parti[1])
parti_flest = antall_sortert[-1] # det siste partiet i lista har flest politikere på stortinget
print(f"Partiet med flest politikere på tinget er {parti_flest[0]} de har {parti_flest[1]}")
 


# 4. Lag et plott som viser en oversikt over partier og antall representanter

import matplotlib.pyplot as plt
parti_liste = list(antall.keys())
antall_liste = list(antall.values())
plt.bar(parti_liste, antall_liste)
plt.xticks(rotation=90) # bonus: roterer teksten på x-aksen 90 grader slik at den er lettere å lese
plt.show() # trenger ikke denne i .ipynb-filer
 


# 5. Hvor mange representanter har hvert parti i gjennomsnitt?

total = 0
for parti in antall:
    total += antall[parti]
snitt = total / len(antall)
print(f"Hvert parti har i gjennomsnitt {snitt} representanter")