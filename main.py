#megoldas
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
def osszeg(cds: [int]) -> int:
    pts: int = 0
    for i in range(len(cds)):
        pts += cds[i]
    return pts

#teszt_esetek