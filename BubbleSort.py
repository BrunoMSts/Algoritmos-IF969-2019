def BubbleSort(lista):
    for a in range(len(lista)):
        for b in range(len(lista)):
            if lista[a] < lista[b]:
                aux = lista[a]
                lista[a] = lista[b]
                lista[b] = aux
    return lista
