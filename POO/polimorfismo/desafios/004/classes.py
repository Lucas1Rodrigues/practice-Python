from rich import print
from rich.panel import Panel
from abc import ABC, abstractmethod
class Mensagem(ABC):
    def __init__(self,msg):
        self._msg = msg
        self._tipo = "on black"
        self._icone = "[bold white]:speech_balloon: Mensagem[/bold white]"

    def mostrar(self):
        print(Panel(f"{self._msg}", title=self._icone, style=self._tipo, border_style="white", width=60))

class Aviso(Mensagem):
    def mostrar(self):
        self._tipo = "on yellow"
        self._icone = "[bold black]:warning: Aviso[/]"
        return super().mostrar()        

        
class Erro(Mensagem):
    def mostrar(self):
        self._tipo = "on red"
        self._icone = "[bold white]:no_entry_sign: Erro[/bold white]"
        return super().mostrar()