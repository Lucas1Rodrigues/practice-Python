class Carrinho:
    def __init__(self,produtos:list = None):
        self.produtos = produtos if produtos else []

    @property
    def total(self):
        self.produtos = sum(p.preco for p in self.produtos else [])

    def __str__(self):
        return f'---------------------------------\n Total: {self.total}'

    def __iadd__(self, other):
        if isinstance(other, Produto):
            return Carrinho(self.produtos + [other])
        elif isinstance(other,Carrinho):
            return Carrinho(self.produtos + other.produtos)
        else:
            raise TypeError("voce tentou adicionar inválido no carrinho")
    
class Produto:
    def __init__(self,nome = '', preco:float = 0):
        self.nome = nome
        self.valor = preco

    def __str__(self):
        return f'{self.nome}(R${self.valor:,.2f})'
    