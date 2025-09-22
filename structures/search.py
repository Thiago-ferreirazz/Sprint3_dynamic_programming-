def busca_sequencial(lista, valor):  # O(n)
    for item in lista:
        if item['nome'].lower() == valor.lower():
            return item
    return None

def busca_binaria(lista, valor):  # O(log n)
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio].lower() == valor.lower():
            return True
        elif lista[meio].lower() < valor.lower():
            inicio = meio + 1
        else:
            fim = meio - 1
    return False
