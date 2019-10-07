def SelectionSort(lista):
    for a in range(len(lista)):
        minimo = a
        for b in range(len(lista)-a):
            if lista[b+a] < lista[minimo]:
                minimo = b+a
                
        if lista[a] != lista[minimo]:
            lista[a], lista[minimo] = lista[minimo], lista[a]
    return lista
