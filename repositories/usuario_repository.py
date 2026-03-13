from database.database import conectar


def cadastrar_usuario(nome, username, senha):

    conn = conectar()
    cursor = conn.cursor()

    sql = """
    INSERT INTO usuarios (nome, username, senha)
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (nome, username, senha))

    conn.commit()

    cursor.close()
    conn.close()


def buscar_usuario_por_username(username):

    conn = conectar()
    cursor = conn.cursor()

    sql = "SELECT * FROM usuarios WHERE username = %s"

    cursor.execute(sql, (username,))

    usuario = cursor.fetchone()

    cursor.close()
    conn.close()

    return usuario