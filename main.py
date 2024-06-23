# from fastapi import FastAPI
# from pydantic import BaseModel

# class Inputs(BaseModel):
#     inp: int
#     inp2: str

# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

# @app.post('/exemplo_2')
# def exemplo_2(inputs: Inputs) -> str:
#     return inputs.inp2

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Livro(BaseModel):
    id: int
    título: str
    autor: str

livros = [
    Livro(id=1, título='O Senhor dos Anéis - A Sociedade do Anel', autor='J.R.R Tolkien'),
    Livro(id=2, título='Harry Potter e a Pedra Filosofal', autor='J.K Rowling'),
    Livro(id=3, título='Hábitos Atômicos', autor='James Clear')
]

@app.get('/livros')
def obter_livros():
    return livros

#ober livro
@app.get('/livros/{id}')
def obter_livros(id : int):
    for livro in livros:
        if livro.id ==id:
            return livro
    return {"erro": "Livro não encontrado"}

#editar 
@app.put('/livros/{id}')
def editar_livro(id: int, livro_alterado: Livro):
    for indice, livro in enumerate(livros):
        if livro.id == id:
            livros[indice] = livro_alterado
            return livros[indice]

#criar 
@app.post('/livros')
def incluir_novo(novo_livro: Livro):
    livros.append(novo_livro)
    return novo_livro


@app.delete('/livros/{id}')
def excluir_livro(id: int):
    for indice, livro in enumerate(livros):
        if livro.id == id:
            del livros[indice]
            return {"message": "Livro excluído com sucesso"}
    raise HTTPException(status_code=404, detail="Livro não encontrado")