from app.models import db
from app.models.user import User


def create_tables():
    with db:
        db.create_tables([User])
        # Assim o Peewee não tenta recriar uma tabela já existente.
        db.create_tables([User], safe=True)


def create_admin():
    """Cria o usuario root (admin do sistema)"""
    admin_username = "admin"

    # Verifica se existe algum usuario no banco de dados com o nome admin_username.
    # Se nao existir ele irá criar um novo.
    if not User.select().where(User.username == admin_username).exists():

        admin = User(
            fullname="Salvador Eduardo Tomocene",
            username=admin_username,
            email="admin@email.com",
            contact="",
            position="Administrador",
            role="admin",
        )
        admin.set_password("admin123")
        admin.save()
        print("Usuário admin criado com sucesso (user = admin / senha = admin123")
    else:
        print("Usuaŕio admin já existe!")


if __name__ == "__main__":
    create_tables()
    create_admin()
