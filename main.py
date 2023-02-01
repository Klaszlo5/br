#megoldas
def eredmeny(jatekos: [int], gepl: [int]):
    if lapok_osszege(jatekos) > 21:
        print("Játékos vesztett")
    if gep_pont > 21:
    if lapok_osszege(gepl) > 21:
        print("Gép vesztett")


def osszeg(cds: [int]) -> int:
    pts: int = 0
    for i in range(len(cds)):
        pts += cds[i]
    return pts

#teszt_esetek