def busca_sequencial(lista, valor):
    """Busca sequencial - O(n)"""
    resultados = []
    for item in lista:
        if item['item'].lower() == valor.lower():
            resultados.append(item)
    return resultados


def busca_binaria(lista, valor):
    """Busca binária - O(log n) - Requer lista ordenada por nome"""
    inicio, fim = 0, len(lista) - 1
    resultados = []

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio]['item'].lower() == valor.lower():
            # Encontrou uma ocorrência, agora busca todas as ocorrências
            resultados.append(lista[meio])
            # Verifica à esquerda
            i = meio - 1
            while i >= 0 and lista[i]['item'].lower() == valor.lower():
                resultados.append(lista[i])
                i -= 1
            # Verifica à direita
            i = meio + 1
            while i < len(lista) and lista[i]['item'].lower() == valor.lower():
                resultados.append(lista[i])
                i += 1
            return resultados
        elif lista[meio]['item'].lower() < valor.lower():
            inicio = meio + 1
        else:
            fim = meio - 1
    return resultados