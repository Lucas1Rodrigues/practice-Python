class Carrinho:
    def __init__(self):
        self.produto = [Produto()]
        self.total = 0

    @property
    def total(self):
        return self.total

    def __str__(self):
        return f'---------------------------------\n Total: {self.total}'

    def __iadd__(self, other):
        if other < 0:
            raise ValueError("Valores nao podem ser negativos")
        if not isinstance(other,int) or not isinstance(other,float):
            raise ValueError("Digite um valor válido")
        else:
            self.total += other
    
class Produto:
    def __init__(self,nome = '', valor:float = 0):
        self.nome = nome
        self.valor = valor
    