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
    if zahl > 0 and zahl <= 5:
        return bewertungsNamen[zahl]
    
    else:
        raise InvalidSchnitzel