from abc import ABC, abstractmethod
from time import sleep
class Pagamento(ABC):
    def __init__(self,valor:float = 0):
        self._valor = valor

    @property
    def fvalor(self):
        return f"R${self._valor:,.2f}"
    
    @valor.setter
    def valor(self,valor):
        if valor < 0: 
            raise ValueError("O valor nao pode ser negativo")
        else:
            self._valor = valor

    @abstractmethod
    def pagar(self,valor):
        print(f'Pagamento CONFIRMADO de R$ {self.valor:,.2f} no {self.__class__.__name__}')

class Boleto(Pagamento):
    def pagar(self, valor):
        print("Gerando código de barras...")
        sleep(1)
        super().pagar(valor)

class Pix(Pagamento):
    def pagar(self, valor):
        print("Gerando QR Code Pix...")
        sleep(1)
        super().pagar(valor)

class Credito(Pagamento):
    def pagar(self, valor):
        print("Validando operadora do cartão...")
        sleep(1)
        super().pagar(valor)

def finalizarCompra(pagamento,valor):
    try:
        pagamento.valor = valor       
        pagamento.pagar(valor)
    except:
        raise ValueError("algo deu errado!")
