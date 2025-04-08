from repository.locadora_repository import LocadoraRepository
from model.locadora_dto import Jogos as JogosDTO
from sqlalchemy.orm import Session

def criar_jogo(jogo: JogosDTO, db: Session):
    repo = LocadoraRepository(db)
    return repo.save_jogo(jogo)

def listar_jogo(db: Session):
    repo = LocadoraRepository(db)
    return repo.find_all()

def encontrar_por_codigo(codigo_de_barras: int, db: Session):
    repo = LocadoraRepository(db)
    return repo.find_user_by_codigo_de_barras(codigo_de_barras)

def alterar_jogo(codigo_de_barras: int, jogo: JogosDTO, db: Session):
    repo = LocadoraRepository(db)
    return repo.alterar_jogo(codigo_de_barras, jogo)

def mostrar_ultimo_jogo_inserido(db: Session):
    repo = LocadoraRepository(db)
    return repo.ultimo_jogo_inserido()