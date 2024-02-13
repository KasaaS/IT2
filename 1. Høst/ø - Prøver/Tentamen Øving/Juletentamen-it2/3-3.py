
def fjern_utsolgte(handleliste, utsolgte):

    ny_handleliste = handleliste.copy()

    for utsolgt in utsolgte:
        ny_handleliste.remove(utsolgt)
        return handleliste


print(fjern_utsolgte(["melk", "brus", "pasta"], ["brus", "kanel"]))