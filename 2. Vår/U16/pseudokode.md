# Pseudokode

- en måte å beskrive en algoritme eller et program ved naturlig språk
- brukes ofte som verktøy for ¨planlegge og designe algoritmer før de faktisk blir kodet i et bestemt programmerinsspråk
- gør det lettere å kommunisere og samarbeide med andre programmerere, samt teste og feilsøke algoritmer før de blir kodet
- en god måte å lære grunnleggende programmeringskonsepter på, da det kan hjelpe deg med å forstå hvordan ulike instruksjoner og logiske utrykk fungerer sammen for å løse et bestemt problem.

## Eksempel: Penger tjent på spotify

> En algoritme som regner ut hvor mye penger vi tjener på spotify

```pseudo
Hent inn antall streams
Hvis antall streams er større enn 30 000 000:
    Returner antall streams multiplisert med 70%
Eller hvis antall streams er større enn 1 400 000:
    Returner antall streams multiplisert med 40%
Ellers:
    Returner 0
```


> En algoritme som regner ut hvor mye penger vi tjener på spotify (med nøkkelord)

```pseudo
SET antall_streams TO READ "Hvor mange streams?"
IF antall_streams GREATER THAN 30 000 000:
    THEN DISPLAY antall_streams * 0.7
ELSE IF antall_streams GREATER THAN 1 400 000:
    THEN DISPLAY antall_streams * 0.4
ELSE DISPLAY 0

```


```python
# Oppgave: Skriv algoritmen i vanlig python-kode:
streams = int(input("Hvor mange streams?"))

def penger_tjent(streams):
    if streams > 30_000_000:
        return streams * 0.7
    elif streams > 1_400_000
        return streams * 0.4
    else:
        return 0

penger_tjent(streams)