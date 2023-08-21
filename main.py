class InvalidSchnitzel(Exception):
    pass


bewertungsNamen = {
    5 : "Sehr Gut",
    4 : "Gut",
    3 : "Befriedigend",
    2 : "Ausreichend",
    1 : "Mangelhaft"
}

def bewerte(zahl):
    try:
        zahl = int(zahl)
    except(ValueError):
        raise InvalidSchnitzel
    
    if zahl > 0 and zahl <= 5:
        return bewertungsNamen[zahl]
    else:
        raise InvalidSchnitzel
    
def durchschnitt(zahlen):
    summe = 0
    laenge = 0
    for x in zahlen:
        summe += x
        laenge += 1
        
    ergebnis = summe / laenge
    return ergebnis