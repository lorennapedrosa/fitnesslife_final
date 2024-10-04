SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT NOT NULL,
    data_nascimento DATE NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    tema TEXT NOT NULL,
    perfil INTEGER NOT NULL)
"""

SQL_OBTER_POR_ID = """
    SELECT id, nome, data_nascimento, email, senha, tema, perfil
    FROM usuario
    WHERE id=?
"""

SQL_INSERIR_USUARIO = """
    INSERT INTO usuario 
    (nome, data_nascimento, email, senha, tema, perfil)
    VALUES (?, ?, ?, ?, ?, "default", ?)
"""

SQL_CHECAR_CREDENCIAIS = """
    SELECT id, nome, email, perfil, senha
    FROM usuario
    WHERE email=?
"""

SQL_ATUALIZAR_DADOS = """
    UPDATE usuario
    SET nome=?, data_nascimento=?, email=?, telefone=?
    WHERE id=?
"""


SQL_ATUALIZAR_SENHA = """
    UPDATE usuario
    SET senha=?
    WHERE id=?
"""

SQL_ATUALIZAR_TEMA = """
    UPDATE usuario
    SET tema=?
    WHERE id=?
"""

SQL_EXCLUIR_USUARIO = """
    DELETE FROM usuario
    WHERE id=?
"""