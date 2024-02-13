# Simulering paradise hotell



def main():
    pott = 0
    print("Velkommen til troskapstesten")
    for i in range(10):
        pott += 10000
        print(f"runde {i + 1}: {pott},-")
        
        if snill_spiller(pott) == False:
            print("snill spiller kastet kula")
            break

        elif slem_spiller(pott) == False:
            print("slem spiller kastet kula")
            break


def snill_spiller(beløp):
    return True 

def slem_spiller(beløp):
    return False

def slu_spiller(beløp):
    if beløp >= 50000:
        return False
    else:
        return True


main()
