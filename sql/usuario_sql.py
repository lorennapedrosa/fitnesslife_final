SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        data_nascimento DATE NOT NULL,
        email VARCHAR(100) NOT NULL,
        senha VARCHAR(100) NOT NULL,
        perfil INTEGER NOT NULL
    )
"""

SQL_INSERIR = """
    INSERT INTO usuario (nome, data_nascimento, email, senha, perfil)
    VALUES (?, ?, ?, ?, ?)
"""

SQL_OBTER_SENHA_POR_EMAIL = """
    SELECT senha
    FROM usuario
    WHERE email = ?
"""

SQL_OBTER_DADOS_POR_EMAIL = """
    SELECT id, nome, data_nascimento, email, perfil
    FROM usuario
    WHERE email = ?
"""

SQL_OBTER_POR_ID = """
    SELECT id, nome, data_nascimento, email, perfil
    FROM usuario
    WHERE id = ?
"""

SQL_ATUALIZAR_DADOS = """
    UPDATE usuario
    SET nome = ?, data_nascimento = ?, email = ?
    WHERE id = ?
"""

SQL_ATUALIZAR_SENHA = """
    UPDATE usuario
    SET senha = ?
    WHERE id = ?
"""

SQL_EXCLUIR = """
    DELETE FROM usuario
    WHERE id = ?
"""