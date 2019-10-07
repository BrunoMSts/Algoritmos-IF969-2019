def QuickSort(lista):
    if lista == []: return []
    else:
        pivo = lista.pop(0)
        return QuickSort([x for x in lista if x <= pivo]) + [pivo] + QuickSort([y for y in lista if y > pivo])

print(QuickSort([6,5,3,8,0,10]))
