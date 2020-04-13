def remove_repetidos(lista):
        global ordem
        semRepetir = []
        i = 0
        while i < len(lista):
                if lista[i] not in semRepetir:
                        semRepetir.append(lista[i])
                i += 1
        semRepetir.sort()
        return semRepetir


'''def ordenar_lista(semRepetir):
        global ordem
        ordem = []
        mini = 0
        positionmin = 0
        x = 0
        while len(semRepetir) > 1:
                while x < len(semRepetir):
                        if x == 0:
                                mini = semRepetir[x]
                                x += 1
                        else:
                                if semRepetir[x] < mini:
                                        mini = semRepetir[x]
                                        positionmin = x
                                else:
                                        if len(semRepetir) == 2:
                                                positionmin = 0
                                x += 1
                x = 0
                ordem.append(mini)
                semRepetir.pop(positionmin)
        while len(semRepetir) == 1:
                mini = semRepetir[0]
                ordem.append(mini)
                semRepetir.pop(0)

        return ordem'''



