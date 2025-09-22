from structures.queue import Queue
from structures.stack import Stack


class RegistroConsumo:
    def __init__(self):
        self.fila_retiradas = Queue()
        self.pilha_retiradas = Stack()
        self.insumos = []

    def registrar_retirada(self, item_nome, quantidade, data):
        retirada = {"item": item_nome, "quantidade": quantidade, "data": data}
        self.fila_retiradas.enqueue(retirada)
        self.pilha_retiradas.push(retirada)
        return retirada

    def get_todas_retiradas(self):
        return list(self.fila_retiradas)