
# Input er en funksjon som tar inn argumentet og returnerer det brukeren svarer

navn = input("Hva heter du? (fornavn og etternavn) \n")
fornavn, etternavn = navn.split(" ") #splitter sånn at vi splitter etter hvert mellomrom

fornavn = fornavn.capitalize()
navn = navn.title()

print("hallo", fornavn, "og", etternavn)
print("ditt navn er", navn)

