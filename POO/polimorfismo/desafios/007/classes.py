class Usuario:
    def __init__(self,nome, email):
        self.nome = nome
        self.email = email
class Aluno:
    def init(self,nome,curso,serie):
        self.nome = nome
        self.curso = curso
        self.serie = serie

class JSON:
    def exportar(self,dados):
        return f"exportantando dados de {dados} para json"

class XML:
    def exportar(self,dados):
        from json import dumps

def exportar_dados(formato:exportar,dados):
    print(formato.exportar(dados))