from database.database import conectar
from database.database import conectar

def registrar_compra(usuario_id, jogo_id):

    conn = conectar()
    cursor = conn.cursor()

    sql = """
    INSERT INTO compras (usuario_id, jogo_id, data_compra)
    VALUES (%s, %s, NOW())
    """

    cursor.execute(sql, (usuario_id, jogo_id))

    conn.commit()

    cursor.close()
    conn.close()


def listar_compras_usuario(usuario_id):

    conn = conectar()
    cursor = conn.cursor()

    sql = """
    SELECT jogos.nome, jogos.preco, compras.data_compra
    FROM compras
    JOIN jogos ON compras.jogo_id = jogos.id
    WHERE compras.usuario_id = %s
    """

    cursor.execute(sql, (usuario_id,))

    compras = cursor.fetchall()

    cursor.close()
    conn.close()

    return compras