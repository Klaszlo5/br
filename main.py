import random
def szamol(kartyk):
    ret = 0
    for i in range(len(kartyk)):
        ret += kartyk[i]
    return ret
def osszegz(kartyk):
    kezben = []
    for i in range(2):
        random.shuffle(kartyk)
        kartyid = kartyk.pop()
        if kartyid == 11:kartyid = "J"
        if kartyid == 12:kartyid = "Q"
        if kartyid == 13:kartyid = "K"
        if kartyid == 14:kartyid = "A"
        kezben.append(kartyid)
    return kezben
def ujra():
    megint = input("akarsz újra játszani? (i/n) : ").lower()
    if megint == "i":
        gep_kez = []
        jatekos_kez = []
        kartyak = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*8
        oszto()
    else:
        print("köszi a játékot!")
        exit()
def oszto(jatekos,jatekos2):
    ertek = szamol(jatekos)
    ertek2 = szamol(jatekos2)
    if ertek <= 21 and ertek2 <= 21:
        if ertek2 > ertek:
            ir = "A játékos1 nyert"
        elif ertek > ertek2:
            ir = "játékos2(gép) nyert"
        elif ertek2 == ertek:
            if len(jatekos) < len(jatekos2):
                ir = "A játékos nyert"
            elif len(jatekos) > len(jatekos2):
                ir = "játékos2(gép) nyert"
            else:
                ir = "nem nyert senki"
    if ertek2 > 21:
        ir = "játékos1 vesztett"
    if ertek > 21:
        ir = "játékos2(gép) a vesztes"
    if ertek2 > 21 and ertek > 21:
        ir = "egyik se nyert"

    return ir
def osszesk(kezben):
    osszesk = 0
    for karty in kezben:
        if karty == "J" or karty == "Q" or karty == "K":
            osszesk+= 10
        elif karty == "A":
            if osszesk >= 11: osszesk+= 1
        else: osszesk+= 11
        osszesk += karty
    return osszesk
def talal(kezben):
	kartyk = kezben.pop()
	if kartyk == 11:kartyk = "J"
	if kartyk == 12:kartyk = "Q"
	if kartyk == 13:kartyk = "K"
	if kartyk == 14:kartyk = "A"
	kezben.append(kartyk)
	return kezben
def jatekos1veszitnagyobb():
    jatekos = [10,10,5]
    jatekos2 = [5,10]
    eredm = "játékos vesztett"
    eredm2 = oszto(jatekos,jatekos2)
    print("játékos vesztett nagyobbb értékkel: ",end="")
    if eredm2 == eredm:
        print("teszt sikeres")
    else:
        print("a teszt nem megy")
def jatekos1veszitkissebb():
    jatekos = [10,5]
    jatekos2 = [10,10]
    eredm = "A gép nyert"
    eredm2 = oszto(jatekos,jatekos2)
    print("játékos vesztett kissebb értékkel: ",end="")
    if eredm2 == eredm:
        print("teszt sikeres")
    else:
        print("a teszt nem megy")

def jatekos1veszitkevesebb():
    jatekos = [10,5,5]
    jatekos2 = [10,10]
    eredm = "A gép nyert"
    eredm2 = oszto(jatekos,jatekos2)
    print("játékos vesztett több lappal: ",end="")
    if eredm2 == eredm:
        print("teszt sikeres")
    else:
        print("a teszt nem megy")

def jatekos2veszitnagyobb():
    jatekos = [10,10,]
    jatekos2 = [5,10, 10]
    eredm = "játékos2 vesztett"
    eredm2 = oszto(jatekos,jatekos2)
    print("játékos2 vesztett nagyobb értékkel: ",end="")
    if eredm2 == eredm:
        print("teszt sikeres")
    else:
        print("a teszt nem megy")

def jatekos2veszitkissebb():
    jatekos = [10,10]
    jatekos2 = [10,5]
    eredm = "játékos nyert"
    eredm2 = oszto(jatekos,jatekos2)
    print("játékos2 vesztett kevesebb lappal: ",end="")
    if eredm2 == eredm:
        print("teszt sikeres")
    else:
        print("a teszt nem megy")

def jatekos2veszitkevesebb():
    jatekos = [10,4,6]
    jatekos2 = [10,4,6]
    eredm = "játékos nyert"
    eredm2 = oszto(jatekos,jatekos2)
    print("játékos2 vesztett kevesebb lappal: ",end="")
    if eredm2 == eredm:
        print("teszt sikeres")
    else:
        print("a teszt nem megy")
def dontetlenkevesebb():
    jatekos = [10,10]
    jatekos2 = [10,10]
    eredm = "döntetlen, nem nyert senki"
    eredm2 = oszto(jatekos,jatekos2)
    print("döntetlen, kevesebb lapos: ",end="")
    if eredm2 == eredm:
        print("teszt sikeres")
    else:
        print("a teszt nem megy")

def dontetlennagyobb():
    jatekos = [11,9]
    jatekos2 = [11,9]
    eredm = "nem nyert senki"
    eredm2 = oszto(jatekos,jatekos2)
    print("döntetlen, nagyobb érték mint 21: ",end="")
    if eredm2 == eredm:
        print("a teszt sikeres")
    else:
        print("a teszt nem megy")

def teszt_tesztesetek():
    jatekos1veszitnagyobb()
    jatekos1veszitkissebb()
    jatekos1veszitkevesebb()
    jatekos2veszitnagyobb()
    jatekos2veszitkissebb()
    jatekos2veszitkevesebb()
    osszegz()
    ujra()
    osszesk()
    talal()
    dontetlenkevesebb()
    dontetlennagyobb()

teszt_tesztesetek()
