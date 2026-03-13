from database.database import conectar


def cadastrar_jogo(nome, preco, estoque):

    conn = conectar()
    cursor = conn.cursor()

    sql = """
    INSERT INTO jogos (nome, preco, estoque)
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (nome, preco, estoque))

    conn.commit()

    cursor.close()
    conn.close()


def listar_jogos():

    conn = conectar()
    cursor = conn.cursor()

    sql = "SELECT * FROM jogos"

    cursor.execute(sql)

    jogos = cursor.fetchall()

    cursor.close()
    conn.close()

    return jogos


def buscar_jogo_por_id(jogo_id):

    conn = conectar()
    cursor = conn.cursor()

    sql = "SELECT * FROM jogos WHERE id = %s"

    cursor.execute(sql, (jogo_id,))

    jogo = cursor.fetchone()

    cursor.close()
    conn.close()

    return jogo


def atualizar_estoque(jogo_id, novo_estoque):

    conn = conectar()
    cursor = conn.cursor()

    sql = "UPDATE jogos SET estoque = %s WHERE id = %s"

    cursor.execute(sql, (novo_estoque, jogo_id))

    conn.commit()

    cursor.close()
    conn.close()