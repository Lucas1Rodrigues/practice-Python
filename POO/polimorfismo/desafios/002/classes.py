from abc import ABC, abstractmethod
class Arquivo(ABC):
    def __init__(self,nome:str = '', tamanho:float = 0):
        self.nome = nome
        self._extensao = ''
        self.tamanho = tamanho

    @property
    def nome_completo(self):
        return f'{self.nome}.{self._extensao} ({self.tamanho:.1f}MB)'

    @nome_completo.setter
    def nome_completo(self,nome,tamanho):
        if nome | tamanho is None:
            raise ValueError("Digite um valor válido.")
        else:
            self.nome = nome
            self.tamanho = tamanho
    
    @abstractmethod
    def abrir(self):
        pass

        
class PDF(Arquivo):
    def abrir(self):
        self._extensao = 'pdf'
        print(f'Abrindo {self.nome}.{self._extensao} ({self.tamanho:.1f}MB) no adobe reader')
    
class Doc(Arquivo):
    def abrir(self):
        self._extensao = 'docx'
        print(f'Abrindo {self.nome}.{self._extensao} ({self.tamanho:.1f}MB) no microsft Word')

def abrirArquivo(arquivo):
    try:
        arquivo.abrir()
    except:
        raise PermissionError("Nao conseguimos abrir o arquivo...")