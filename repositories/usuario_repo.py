from datetime import date
from typing import Optional
from dtos.usuario_autenticado import UsuarioAutenticado
from models.usuario_model import Usuario
from sql.usuario_sql import *
from util.auth import conferir_senha
from util.db import obter_conexao


class UsuarioRepo:
    @classmethod
    def criar_tabela(cls):
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_CRIAR_TABELA)

    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Usuario]:
        with obter_conexao() as db:
            cursor = db.cursor()
            dados = cursor.execute(
                SQL_OBTER_POR_ID, (id,)).fetchone()
            if dados:
                usuario = Usuario(*dados)
                return usuario
            return None
        
    @classmethod
    def inserir(cls, usuario: Usuario) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            resultado = cursor.execute(SQL_INSERIR_USUARIO,
                (usuario.nome,
                 usuario.descricao_pessoal,
                 usuario.email,
                 usuario.senha,
                 usuario.perfil))
            return resultado.rowcount > 0
        
    @classmethod
    def atualizar_dados(cls, usuario: Usuario) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            resultado = cursor.execute(
                SQL_ATUALIZAR_DADOS, (
                    usuario.nome, 
                    usuario.email, 
                    usuario.data_nascimento,
                    usuario.descricao_pessoal, 
                    usuario.id))
            return resultado.rowcount > 0
    
    @classmethod
    def atualizar_senha(cls, id: int, senha: str) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            resultado = cursor.execute(
                SQL_ATUALIZAR_SENHA, (senha, id))
            return resultado.rowcount > 0
    
    @classmethod
    def atualizar_tema(cls, id: int, tema: str) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            resultado = cursor.execute(
                SQL_ATUALIZAR_TEMA, (tema, id))
            return resultado.rowcount > 0
      
    @classmethod
    def checar_credenciais(cls, email: str, senha: str) -> Optional[UsuarioAutenticado]:
        with obter_conexao() as db:
            cursor = db.cursor()
            (id, nome, email, perfil, senha_hash) = cursor.execute(
                SQL_CHECAR_CREDENCIAIS, (email,)).fetchone()
            if id:
                if conferir_senha(senha, senha_hash):
                    return UsuarioAutenticado(id, nome, email, perfil)
            return None
    
    @classmethod
    def excluir_usuario(cls, id: int) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            resultado = cursor.execute(
                SQL_EXCLUIR_USUARIO, (id,))
            return resultado.rowcount > 0    