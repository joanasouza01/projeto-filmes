from fastapi import FastAPI
import funcao

#rodar o fastapi:
#python -m uvicorn api:app --reload

#testar api FastAPI
#/docs > documentação swagger
#/redoc > documentação redoc

#iniciar o fastapi
app = FastAPI(title="Gerenciador de Filmes")

#GET = pegar / listar
#POST = criar / enviar
#PUT = atualizar 
#DELETE = deletar

@app.get("/")
def home():
    return {"mensagem": "quero café prof☕"}

@app.post("/filmes")
def criar_filmes(titulo: str, genero: str, ano: int, avaliacao: float):
    funcao.inserir_filme(titulo, genero, ano, avaliacao)
    return{"mensagem": "Filme adicionado com sucesso!"}

@app.get("/filmes")
def listar_filme():
    filmes = funcao.listar_filme()
    lista = []
    for linha in filmes:
        lista.append({"id": linha[0], 
                      "titulo": linha[1], 
                      "genero": linha[2], 
                      "ano": linha[3], 
                      "avaliacao": linha[4]
                      })
    return{"filmes": lista}

