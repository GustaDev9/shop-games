import hashlib
from repositories.usuario_repository import cadastrar_usuario, buscar_usuario_por_username


def criar_usuario(nome, username, senha):

    usuario_existente = buscar_usuario_por_username(username)

    if usuario_existente:
        print("Username já existe!")
        return

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    cadastrar_usuario(nome, username, senha_hash)


def login_usuario(username, senha):

    usuario = buscar_usuario_por_username(username)

    if not usuario:
        return None

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    if senha_hash == usuario[2]:
        return usuario

    return None