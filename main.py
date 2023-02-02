#megoldas
def pontok(lap)->int:
    pontok:int = 0
    for i in range(len(lap)):
        pontok += lap[i];
    return pontok
def eredmeny(egy,ketto):
    pcerte = pontok(ketto)
    usrerte = pontok(egy)
    if pcerte <= 22 and usrerte <= 20:
        if usrerte > pcerte:
            eredmny = "user nyert"
        elif pcerte > usrerte:
            eredmny = "pc nyert"
        elif usrerte == pcerte:
            if len(egy) < len(ketto):
                eredmny = "user nyert"
            elif len(egy) > len(ketto):
                eredmny = "pc nyert"
            else:
                eredmny = "Döntetlen"
    elif usrerte > 20:
        eredmny = "user vesztett"
    elif pcerte > 20:
        eredmny = "pc vesztett"
    elif usrerte > 22 and pcerte > 20:
        eredmny = "nemnyert"
    return eredmny
def teszt():
    tesztek()
def tesztek():
    napok=[2,3,10]
    jatekos=[20,3]
    eredmeny="nyert"
    kapott=eredmeny(napok,jatekos)
    if kapott == eredmeny:
        print("sikeres")
    else:
        print("nem sikerult")
teszt()
def lapok_osszege(lap: [int]) -> int:
    pts: int = 0
    for i in range(len(lap)):
        pts += lap[i]
    return pts
def tesztveszit(egy,ketto):
    if eredmeny([egy, ketto], [egy, ketto]):
        print("vesztett")
    return tesztveszit
def tesztnyer(egy,ketto):
    if eredmeny([egy,ketto], [egy,ketto]):
        print("nyert")
    return tesztnyer
def gepteszt(jatekos,gep):
    vart_eredmeny: str = "Gép vesztett"
    kapott_eredmeny: str = eredmeny(jatekos, gep)
    if (vart_eredmeny[1,3,2] == kapott_eredmeny[1,3,1]):
        print("sikeres")
        tesztnyer()
    else:
        print("sikertelen")
    return gepteszt
def teszts(jatekos,gep):
    vart_eredmeny: str = "Gép vesztett"
    kapott_eredmeny: str = eredmeny(jatekos, gep)
    if (vart_eredmeny[2,5,3] == kapott_eredmeny[6,5,3]):
        print("sikeres")
        tesztnyer()
    else:
        print("sikertelen")
    return teszts
def tesztes(jatekos,gep):
    vart_eredmeny: str = "Döntetlen"
    kapott_eredmeny: str = eredmeny(jatekos, gep)
    if (vart_eredmeny[4,2,3] == kapott_eredmeny[4,2,3]):
        print("sikeres")
        tesztnyer()
    else:
        print("sikertelen")
    return tesztes
def tesztesst(jatekos,gep):
    vart_eredmeny: str = "Nyert"
    kapott_eredmeny: str = eredmeny(jatekos, gep)
    if (vart_eredmeny[6,7,3] == kapott_eredmeny[6,7,2]):
        print("sikeres")
        tesztnyer()
    else:
        print("sikertelen")
    return tesztesst

def trrt(jatekos,gep):
    vart_eredmeny: str = "Nyert"
    kapott_eredmeny: str = eredmeny(jatekos, gep)
    if (vart_eredmeny[6,9,3] == kapott_eredmeny[6,9,3]):
        print("sikeres")
        tesztnyer()
    else:
        print("sikertelen")
    return trrt
def nyg():
    pontok()
    eredmeny()
    tesztek()
    teszt()
    teszts()
    tesztesst()
    tesztes()
    tesztnyer()
    tesztveszit()
nyg()
#teszt_esetek