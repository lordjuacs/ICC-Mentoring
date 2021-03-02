def max_enf(matriz):
    gmax = 0
    pos = 0
    for j in range(len(matriz[0])):
        tmax = 0
        for lista in matriz:
            tmax += lista[j]
        if tmax > gmax:
            gmax = tmax
            pos = j
    return pos

def max_ciu(matriz):
    gmax = 0
    pos = 0
    for i in range(len(matriz)):
        if sum(matriz[i]) > gmax:
            gmax = sum(matriz[i])
            pos = i
    return pos


dic = {0: 'Gripe', 1: 'Influenza', 2: 'Colera'}
matriz = [[200, 460, 340], [620, 180, 200], [530, 350, 250]]
print(max_ciu(matriz))