from livros import *

def obter_livros_id(id: int) -> Livro:
    for livro in livros:
        if livro.id == id:
            return livro
        
def editar_livro(id, livro_alterado: Livro)-> dict:
    for indice, livro in enumerate(livros):
        if livro.id == id:
            livros[indice] = livro_alterado
            return livro      

def incluir_novo_livro(novo_livro:Livro):
   novo_livro.id = len(livros) + 1
   livros.append(novo_livro)
   return novo_livro

def deletar_livro(id):
    for indice, livro in enumerate(livros):
            if livro.id == id:
                 livros.pop(indice)
                 return {"message": "Livro excluído com sucesso"}
    return {}

def editar_nome(id, novo_titulo: str):
    for indice, livro in enumerate(livros):
        if livro.id == id:
            livros[indice].título = novo_titulo
            return novo_titulo


    