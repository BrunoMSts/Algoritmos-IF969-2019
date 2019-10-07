def MergeSort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista)
    if (fim - inicio) > 1:
        meio = (fim + inicio) // 2
        MergeSort(lista, inicio, meio)
        MergeSort(lista, meio, fim)
        Merge(lista, inicio, meio, fim)
    return lista
def Merge(lista,inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    l, r = 0, 0
    for k in range(inicio, fim):
        if l >= len(left):
            lista[k] = right[r]
            r += 1
        elif r >= len(right):
            lista[k] = left[l]
            l += 1
        elif left[l] < right[r]:
            lista[k] = left[l]
            l += 1
        else:
            lista[k] = right[r]
            r+= 1
        
