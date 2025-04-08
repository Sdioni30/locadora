from pydantic import BaseModel, Field
from datetime import datetime

class Jogos(BaseModel):
    nome: str 
    classificacao_idade: int 
    preco: float
    codigo_de_barras: int 
    disponivel: bool
    data: datetime = Field(default_factory=datetime.now)

class Funcionario(BaseModel):
    nome: str
    cpf: str
    pis: str
    faltas: int 
    
