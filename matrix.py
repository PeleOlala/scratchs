def symetrie_horizontale(ma):
    return [ma[i] for i in range(len(ma)-1,-1,-1)]

def antisymetrique(matrice):
    res = True
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            res = res and matrice[i][j] == -matrice[j][i]
    return res

def trace(matrice):
    tr=0
    for i in range(len(matrice)):
        tr+=matrice[i][i]
    return tr
