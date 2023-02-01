#megoldas
def pontok(lap)->int:
    pontok:int = 0
    for i in range(len(lap)):
        pontok += lap[i];
    return pontok

def osszeg(cds: [int]) -> int:
    pts: int = 0
    for i in range(len(cds)):
        pts += cds[i]
    return pts

#teszt_esetek