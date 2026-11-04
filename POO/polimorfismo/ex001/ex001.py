#aprendendo polimorfismo exemplos 
from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self,nome):
        self.nome = nome

    @abstractmethod
    def emitirSom(self):
        pass

class cachorro(Animal):
    def emitirSom(self):
        print("AU! AU!")
    
class pato(Animal):
    def emitirSom(self):
        print("QUA! QUA!")
    
class gato:
    pass
class galinha:
    pass