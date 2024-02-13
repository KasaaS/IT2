# program for reisekarantene

# dersom vaksinert - 0 dager
# dersom uvaksinert og rød/oransje - 10 dager
# dersom uvaksinert og grønn - 3 dager



# if vaksinert:
#     dager = 0

# elif vaksinert == False:
#     if land == "grønn":
#         dager = 3
#     else:
#         dager = 10


# print(dager, "dager karantenetid")





def karantene(vaksinert, farge):
    if vaksinert:
        return 0
    elif farge == "rød" or farge == "oransje":
        return 10
    elif farge == "grønn":
        return 3


print(karantene(True, "rød"), "dager")