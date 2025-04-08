from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from repository.locadora_repository import LocadoraRepository
from config.connect_db import get_session
from http import HTTPStatus
from model.locadora_dto import Jogos as JogosDTO
import service.jogo_service as jogo_service


router = APIRouter()


@router.get("/jogos")
def listar_jogos(db: Session = Depends(get_session)):
    return jogo_service.listar_jogo(db) 

@router.get("/jogos/ultimo")
def mostrar_ultimo_jogo(db: Session = Depends(get_session)):
    return jogo_service.mostrar_ultimo_jogo_inserido(db)
 
@router.get("/jogos/{codigo_de_barras}")
def find_user_by_codigo_de_barras(codigo_de_barras: int,db: Session = Depends(get_session)):
    return jogo_service.encontrar_por_codigo(codigo_de_barras, db)

@router.post("/jogos")
def criar_jogo(jogo: JogosDTO, db: Session = Depends(get_session)):
    return jogo_service.criar_jogo(jogo, db)

@router.put("/jogos/{codigo_de_barras}")
def  alterar_jogo(codigo_de_barras: int,jogo: JogosDTO, db:Session = Depends(get_session)):
    return jogo_service.alterar_jogo(codigo_de_barras, jogo, db)

