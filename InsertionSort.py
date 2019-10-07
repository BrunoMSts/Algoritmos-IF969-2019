def insertion(lista):
	for a in range(len(lista)):
		elemento = lista[a]
		j = a - 1
		while j >= 0 and lista[j] > elemento:
			lista[j + 1] = lista[j]
			j -= 1
		lista[j + 1]= elemento
	return lista


