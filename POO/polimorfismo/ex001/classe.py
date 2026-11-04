from functools import singledispatchmethod
class Analisador:
    @singledispatchmethod
    def analisar(self,valor):
        print(f'{valor} nao é um valor conhecido')

    @analisar.register
    def _(self, valor:str):
        print(f'{valor} é uma cadeia de caracteres')

    @analisar.register
    def _(self,valor:int):
        print(f'{valor} é um valor do tipo inteiro')

    @analisar.register
    def _(self,valor:float):
            print(f'{valor} é um valor do tipo float (real)')
    
    @analisar.register
    def _(self,valor:list|tuple|dict):
            print(f'{valor} é uma colecao de dados')
    