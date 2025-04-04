from pydantic import BaseModel

class Jogos(BaseModel):
    nome: str 
    classificacao_idade: int 
    preço: float
    codigo_de_barras: int 
    disponivel: bool

class Funcionario(BaseModel):
    nome: str
    cpf: str
    pis: str
    faltas: int 
    
