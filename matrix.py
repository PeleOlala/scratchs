def symetrie_horizontale(ma):
    """
    Горизонтальная симметрия
    """
    return [ma[i] for i in range(len(ma)-1,-1,-1)]

def antisymetrique(matrice):
    """
    Проверка является ли матрица ассиметричной
    """
    res = True
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            res = res and matrice[i][j] == -matrice[j][i]
    return res

def trace(matrice):
    """
    сумма всех элементов первой диагонали.
    """
    tr=0
    for i in range(len(matrice)):
        tr+=matrice[i][i]
    return tr
