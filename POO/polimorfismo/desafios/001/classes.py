from abc import ABC, abstractmethod
class Funcionario(ABC):
    def __init__(self,nome,salario=0):
        self.nome = nome
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self,salario):
        if salario is None:
            raise ValueError("Voce precisa digitar um valor")
        else:
            if salario < self.__salario:
                raise TypeError("O Salario nao pode ser inferior ao inicial.")
            else:
                self.__salario = salario

    def calcularBonus(self,bonus):
        return self.salario * bonus

    def __str__(self):
        return f"O salario de {self.nome}: R${self.salario} com um bonus de {self.calcularBonus()}"

class Gerente(Funcionario):
    def calcularBonus(self):
        return super().calcularBonus(0.15)        

class Designer(Funcionario):
    def calcularBonus(self):
        return super().calcularBonus(0.08)

class Desenvolvedor(Funcionario):
    def calcularBonus(self):
        return super().calcularBonus(0.1)