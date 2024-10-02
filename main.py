from fastapi import FastAPI
from typing import List
from funcoes import *
from livros import *

app = FastAPI()

@app.get('/livros')
def obter_livros():
    return livros


#obter o livro 
@app.get('/livros/{id}')
def obter_livros_resquest(id: int):
    livro_achado = obter_livros_id(id)
    return livro_achado


#editar 
@app.put('/livros/{id}')
def editar_livro_resquest(id: int, livro_alterado: Livro):
    editar_livro(id, livro_alterado)

#criar 
@app.post('/novolivro')
def incluir_novo_request(novo_livro: Livro):
    incluir_novo_livro(novo_livro)

#Deletar
@app.delete('/livrosdelet/{id}')
def excluir_livro(id: int):
   deletar_livro(id)


#ALTERA SOMENTE O NOME DO LIVRO 
@app.put('/editartitulo')
def editar_nome_request(id: int, novo_titulo: str):
    editar_nome(id, novo_titulo)

#DELETAR TODOS OS LIVROS 
@app.delete('/deleteall')
def delet_all():
    livros.clear()
    return livros


