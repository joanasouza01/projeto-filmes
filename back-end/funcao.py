from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS filmes (
                id SERIAL PRIMARY KEY,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                ano INTEGER NOT NULL,
                avaliacao REAL
                )
            """)
            conexao.commit()
        except Exception as erro:
            print(f"erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.close()

criar_tabela()

def inserir_filme(titulo, genero, ano, avaliacao):
        conexao, cursor = conectar()
        if conexao:
            try:
                cursor.execute(
                "INSERT INTO filmes (titulo, genero, ano, avaliacao) VALUES (%s, %s, %s, %s)",
                (titulo, genero, ano, avaliacao)
            )
                conexao.commit()
            except Exception as erro:
                print(f"erro ao inserir filmes")
            finally:
                cursor.close()
                conexao.close()

def listar_filme():
        conexao, cursor = conectar()
        if conexao:
            try:
                cursor.execute(
                "SELECT * FROM filmes ORDER BY id"
            )
                return cursor.fetchall()
            except Exception as erro:
                print(f"erro ao tentar listar filmes")
            finally:
                cursor.close()
                conexao.close()

def atualizar_filme(id_filmes, nova_avaliacao):
     conexao, cursor = conectar()
     if conexao:
        try:
            cursor.execute(
            "UPDATE filmes SET avaliacao = %s WHERE id = %s", 
            (nova_avaliacao, id_filmes)
        )
            conexao.commit()
        except Exception as erro:
            print(f"erro ao tentar atualizar filmes")
        finally:
            cursor.close()
            conexao.close()
atualizar_filme(1, 9)

def deletar_filme(id_filmes):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
            "DELETE FROM filmes WHERE id = %s", (id_filmes,)
        )
            conexao.commit()
        except Exception as erro:
            print(f"erro ao tentar deletar filme")
        finally:
            cursor.close()
            conexao.close()
deletar_filme(1)