from datetime import datetime, timedelta
import random

def gerar_historico_simulado(insumos):
    historico = []
    data_base = datetime.now()
    for _ in range(5):
        item = random.choice(insumos)
        retirada = {
            "item": item['nome'],
            "quantidade": random.randint(1, 50),
            "data": data_base - timedelta(days=random.randint(1, 100))
        }
        historico.append(retirada)
    return historico

def gerar_historico_vazio():
    return []
