from http import HTTPStatus
from fastapi import HTTPException
from sqlalchemy import select, desc
from sqlalchemy.orm import Session

from model.jogos import Jogos as JogosDB
from model.locadora_dto import Jogos as JogosDTO

class LocadoraRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def find_all(self):
        return self.session.scalars(select(JogosDB)).all()

    def find_user_by_codigo_de_barras(self, codigo_de_barras: int) -> JogosDB:
        try:
            user = self.session.scalar(
                select(JogosDB).where(JogosDB.codigo_de_barras == codigo_de_barras)
            )
            return user

        except Exception:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail='Erro ao acessar banco de dados.',
            )

    def save_jogo(self, jogo: JogosDTO):
        dados = jogo.model_dump(exclude={"data"})
        novo_jogo = JogosDB(**dados)

        self.session.add(novo_jogo)
        self.session.commit()
        return novo_jogo

    def alterar_jogo(self, jogo: JogosDTO, codigo_de_barras: int) -> JogosDB:
        jogo_existente = self.session.get(JogosDB, codigo_de_barras)
        if not jogo_existente:
            raise HTTPException(status_code=404, detail='O jogo não existe')
        for campo, valor in jogo.model_dump().items():
            setattr(jogo_existente, campo, valor)
        self.session.commit()
        self.session.refresh(jogo_existente)
        return jogo_existente
    
    def ultimo_jogo_inserido(self) -> JogosDB:
        resultado = self.session.scalar(
            select(JogosDB).order_by(desc(JogosDB.data)).limit(1)
        )
        if not resultado:
            raise HTTPException(status_code=500, detail="Houve algum problema")
        return resultado