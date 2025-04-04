from fastapi import FastAPI
from schemas import Jogos
from schemas import Funcionario
from http import HTTPStatus

app = FastAPI()
jogos = [{
        "nome": "CS",
        "classificacao_idade": 14,
        "preço": 0,
        "codigo_de_barras": 10,
        "disponivel": True
        }]



@app.get('/jogos')
def ver_jogos():
    for jogo in jogos:
        print(jogo)
    return jogos

@app.get('/jogos/{codigo_de_barras}')
def jogo_por_cod_de_barras(codigo_de_barras: int):
    for jogo in jogos:
        if jogo["codigo_de_barras"] == codigo_de_barras:
            return jogo

@app.post('/jogos', status_code=HTTPStatus.CREATED)
def adicionar_jogo(item: Jogos):
    novo_jogo = item.model_dump()
    jogos.append(novo_jogo)
    return novo_jogo

