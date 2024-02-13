


def per_stream(land):
    Ordbok =  {"Norge": 0.55,
     "Sverige": 0.44,
     "Finland": 0.44,
     "Danmark": 0.52,
     "Island": 0.62}
    
    if land in Ordbok:
        return Ordbok[land]
    else:
        return 0.24
    


print(per_stream("Norge"))
print(per_stream("Sverige"))
print(per_stream("Finland"))
print(per_stream("Danmark"))
print(per_stream("Island"))
print(per_stream("USA"))