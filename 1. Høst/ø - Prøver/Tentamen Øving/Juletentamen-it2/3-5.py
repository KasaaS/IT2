
def forkort_lagliste(lagliste):
    forkort = []

    for lag in lagliste:
        if lag not in forkort:
            forkort.append(lag)

    return forkort


print(forkort_lagliste(["brann", "molde", "brann"]))



