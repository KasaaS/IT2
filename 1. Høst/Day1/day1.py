fil = open("input.txt")
data = fil.read()
fil.close()

linjer = data.split("\n")



talliste = []

for linje in linjer:
    tall = []
    for bokstav in linje:
        if bokstav.isdigit():
            tall.append(bokstav)
    først_og_sist = tall[0] + tall[-1]

    
    talliste.append(først_og_sist)



mandem = 0
for i in talliste:
    i = int(i)
    mandem = mandem + i

print(mandem)