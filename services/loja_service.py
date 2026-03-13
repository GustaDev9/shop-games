from repositories.jogo_repository import buscar_jogo_por_id, atualizar_estoque
from repositories.compra_repository import registrar_compra


def comprar_jogo(usuario_id, jogo_id):

    jogo = buscar_jogo_por_id(jogo_id)

    if not jogo:
        return "Jogo não encontrado"

    estoque = jogo[3]

    if estoque <= 0:
        return "Jogo sem estoque"

    atualizar_estoque(jogo_id, estoque - 1)
    registrar_compra(usuario_id, jogo_id)

    return "Compra realizada com sucesso!"