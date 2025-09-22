class Insumo:
    def __init__(self, nome, quantidade, validade):
        self.nome = nome
        self.quantidade = quantidade
        self.validade = validade

    def __repr__(self):
        return f"{self.nome} ({self.quantidade}) - validade {self.validade}"