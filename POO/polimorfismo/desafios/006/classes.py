import re
from abc import ABC, abstractmethod
class Validador(ABC):

    @abstractmethod
    def validar(self,texto):
        pass

class Email(Validador):
    def validar(self,texto=''):
        padrao = r'[\w]+@[\w]+\.[\w]{2,}'

        if re.fullmatch(padrao, texto):
            print("Email permitido.")
        else:
            print("Email negado.")
        
class Usuario(Validador):
    def validar(self, texto=''):
        padrao = r'[\a-z\d_]{5,20}'

        if re.fullmatch(padrao, texto):
            print("Usuário permitido.")
        else:
            print("Usuário negado.")

class Senha(Validador): 
    def validar(self, texto=''):
        padrao = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%&*])(?=\S+$).{8,}'

        if re.fullmatch(padrao, texto):
            print("Senha permitida.")
        else:
            print("Senha negada.")

def tentarValidar(Validador,texto):
    try:
        Validador.texto = texto
        Validador.validar(texto)
    except:
        print("Houve algum erro")