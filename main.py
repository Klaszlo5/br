#megoldas
def pontok(lap)->int:
    pontok:int = 0
    for i in range(len(lap)):
        pontok += lap[i];
    return pontok
def eredmeny(egy, ketto):
    napok = pontok(egy)
    jatekos = pontok(ketto)
    for jatekos in range(napok):
        napok[jatekos] += napok[jatekos]
    if napok > 21 and jatekos > 21:
        print("nyer")
    elif napok > 21:
        return "Gép vesztett"
    else:
        return "Játékos vesztett"
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
def tesztnyer(egy,ketto):
    if eredmeny([egy,ketto], [egy,ketto]):
        print("nyert")
def gep(jatekos,gep):
    vart_eredmeny: str = "Gép vesztett"
    kapott_eredmeny: str = eredmeny(jatekos, gep)
    if (vart_eredmeny == kapott_eredmeny)
        print("sikeres")
        tesztnyer()
    else:
        print("sikertelen")
        tesztveszit()
#teszt_esetek