SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome VARCHAR(100) NOT NULL,
    descricao_pessoal TEXT NULL,
    data_nascimento DATE NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL,
    perfil INTEGER NOT NULL,
    verificado INTEGER NOT NULL DEFAULT 0)
"""

SQL_OBTER_POR_ID = """
    SELECT id, nome, descricao_pessoal, data_nascimento, email, senha, perfil
    FROM usuario
    WHERE id=?
"""

SQL_INSERIR_USUARIO = """
    INSERT INTO usuario 
    (nome, email, senha, perfil)
    VALUES (?, ?, ?, ?)
"""

SQL_CHECAR_CREDENCIAIS = """
    SELECT id, nome, email, perfil, senha
    FROM usuario
    WHERE email=?
"""

SQL_ATUALIZAR_DADOS = """
    UPDATE usuario
    SET nome=?, descricao_pessoal=?, data_nascimento=?, email=?
    WHERE id=?
"""

SQL_ATUALIZAR_SENHA = """
    UPDATE usuario
    SET senha=?
    WHERE id=?
"""

SQL_EXCLUIR_USUARIO = """
    DELETE FROM usuario
    WHERE id=?
"""