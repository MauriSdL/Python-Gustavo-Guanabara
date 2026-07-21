from peewee import Model, CharField, DateTimeField
from datetime import datetime
from app.models import db
from passlib.hash import sha256_crypt


# Cria a Classe Base(model base).
class BaseModel(Model):
    class Meta:
        database = db


# legenda:
"""
Propriedade 	        Tipo	    O que faz
----------------------------------------------
null=True	            Boolean	    Permite salvar valor vazio (NULL) no banco.
null=False	            Boolean	    Campo obrigatório. (Padrão)
default="valor"	        Qualquer	Valor padrão caso nada seja informado.
unique=True	            Boolean	    Não permite valores repetidos.
index=True	            Boolean	    Cria um índice para pesquisas mais rápidas.
primary_key=True	    Boolean	    Define o campo como chave primária.
constraints=[]	Lista	Permite     adicionar restrições SQL.
help_text="texto"	    String	    Apenas documentação do campo.
verbose_name="Nome"	    String	    Nome amigável do campo.
column_name="nome"	    String	    Nome da coluna no banco.
db_column="nome"	    String	    Mesmo objetivo do column_name (compatibilidade).
choices=[]	Lista	    Limita os valores possíveis.

"""


# Cria o modelo de users
class User(BaseModel):
    fullname = CharField(max_length=255)
    username = CharField(max_length=50, unique=True)
    email = CharField(max_length=100, unique=True)
    contact = CharField(max_length=20, null=True)
    position = CharField(max_length=100, null=True)
    password = CharField(max_length=255)
    role = CharField(default="user", max_length=20)  # admin/user comun
    created_at = DateTimeField(default=datetime.now)

    # Serve para Cadrastrar novo usuario.
    def set_password(self, password: str):
        self.password_hash = sha256_crypt.hash(password)

    # Serve para verificar Autencidade de senhas(login).
    def verify_password(self, password: str) -> bool:
        return sha256_crypt.verify(password, self.password_hash)

    def __str__(self):
        return f"{self.username} - {self.role}"
