def merge_sort(lista, key=lambda x: x):  # O(n log n)
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], key)
    direita = merge_sort(lista[meio:], key)
    return merge(esquerda, direita, key)

def merge(esquerda, direita, key):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if key(esquerda[i]) <= key(direita[j]):
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def quick_sort(lista, key=lambda x: x):  # O(n log n) médio
    if len(lista) <= 1:
        return lista
    pivo = lista[0]
    menores = [x for x in lista[1:] if key(x) <= key(pivo)]
    maiores = [x for x in lista[1:] if key(x) > key(pivo)]
    return quick_sort(menores, key) + [pivo] + quick_sort(maiores, key)
