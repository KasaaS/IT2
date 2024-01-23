todo = []


def lese():
    fil = open("Todo.txt", "r", encoding="utf-8")
    todo = fil.readlines()
    fil.close()
    for objekt in todo:
        print(objekt)


def Skrive():
    with open("Todo.txt", "w", encoding="utf-8") as fil:
        fil.writelines(todo)




brukerinput =  str(input("Lese eller skrive? \n"))


if brukerinput.lower() == "lese":
    lese()
elif brukerinput.lower() == "skrive":
    mengde = int(input("Hvor mange elementer vil du legge til? \n"))
    for i in range (0,mengde):
        element = str(input(f"hva er ditt {i+1} objekt på listen?\n"))
        todo.append(element + "\n")
    Skrive()
else:
    print("Dette gikk ikke")

