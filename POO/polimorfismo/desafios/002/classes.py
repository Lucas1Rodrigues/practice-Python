from abc import ABC, abstractmethod
class Arquivo(ABC):
    def __init__(self,nome:str = '',extensao='', tamanho:float = 0):
        self.nome = nome
        self._extensao = None
        self.tamanho = tamanho
        self.extensao = extensao

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
    
    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self,ext:str):
        formatos = ['pdf', 'docx']
        ext = ext.lower().strip()
        if ext in formatos:
            self._extensao = ext
        else:
            raise ValueError("Extensao nao encontrada, ou nao permitida")
    
    @abstractmethod
    def abrir(self):
        pass

        
class PDF(Arquivo):
    def __init__(self, nome = '', extensao='', tamanho = 0):
        super().__init__(nome,'pdf', tamanho)
    
    def abrir(self):
        print(f'Abrindo {self.nome}.{self._extensao} ({self.tamanho:.1f}MB) no adobe reader')
    
class Doc(Arquivo):
    def __init__(self, nome = '', extensao='', tamanho = 0):
        super().__init__(nome,'docx', tamanho)
    def abrir(self):
        print(f'Abrindo {self.nome}.{self._extensao} ({self.tamanho:.1f}MB) no microsft Word')

def abrirArquivo(arquivo):
        arquivo.abrir()
