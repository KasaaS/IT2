def andel_til_artist(antall_streams):
    if antall_streams <= 399999:
        return 0
    elif antall_streams <= 29999999:
        return 0.4
    else:
        return 0.7
    
print(andel_til_artist(50000))
print(andel_til_artist(5000000))
print(andel_til_artist(50000000))