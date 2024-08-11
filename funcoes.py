from livros import *

def obter_livros_id(id: int) -> Livro:
    for livro in livros:
        if livro.id == id:
            return livro
# def obter_livros_id(id):
#     for livro in livros:  
#         print(livro.id)
#         if livro.id ==id:
#            print(id)
#            return livro
        
def editar_livro(id, livro_alterado: Livro):
    for indice, livro in enumerate(livros):
        if livro.id == id:
            livros[indice] = livro_alterado
            return livros[indice]       

def incluir_novo_livro(novo_livro:Livro):
    livros.append(novo_livro)
    return novo_livro

def deletar_livro(id):
    for indice, livro in enumerate(livros):
            if livro.id == id:
                del livros[indice]
                return {"message": "Livro excluído com sucesso"}