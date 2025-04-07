import os
os.system("cls")

def lenElenchi(ln,lc):

    lenLN = len(ln)
    LenLC = len(lc)
    d = {}
    a = 0
    if LenLC == LenLC:
        d[ln[lenLN-1]] = lc[a]
        for i in ln:
            a+=1
            d[ln[lenLN-a]] = lc[LenLC-a]
    print(d)

ln = ["Alessio","Carlo","Mauro","Nicola"]
lc = ["3Bi","5Ai","4Ai","3Ai"]

lenElenchi(ln,lc)