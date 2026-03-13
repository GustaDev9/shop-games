from repositories.jogo_repository import cadastrar_jogo, listar_jogos
from services.loja_service import comprar_jogo
from services.usuario_service import criar_usuario, login_usuario
from repositories.compra_repository import listar_compras_usuario


def menu_loja(usuario):

    while True:

        print("\n=== LOJA ===")
        print("1 - Cadastrar jogo")
        print("2 - Listar jogos")
        print("3 - Comprar jogo")
        print("4 - Minhas compras")
        print("0 - Logout")

        opcao = input("Escolha: ")

        if opcao == "1":

            nome = input("Nome do jogo: ")

            preco = float(input("Preço: "))
            if preco < 0:
                print("Preço inválido")
                continue

            estoque = int(input("Estoque: "))
            if estoque < 0:
                print("Estoque inválido")
                continue

            cadastrar_jogo(nome, preco, estoque)

            print("Jogo cadastrado com sucesso!")

        elif opcao == "2":

            jogos = listar_jogos()

            print("\n=== LISTA DE JOGOS ===")

            for jogo in jogos:
                print(f"ID: {jogo[0]} | Nome: {jogo[1]} | Preço: {jogo[2]} | Estoque: {jogo[3]}")

        elif opcao == "3":

            jogo_id = int(input("Digite o ID do jogo: "))

            resultado = comprar_jogo(usuario[0], jogo_id)

            print(resultado)

        elif opcao == "4":

            compras = listar_compras_usuario(usuario[0])

            print("\n=== MINHAS COMPRAS ===")

            if not compras:
                print("Nenhuma compra realizada")
                continue

            for compra in compras:
                print(f"Jogo: {compra[0]} | Preço: {compra[1]} | Data da compra: {compra[2]}")

        elif opcao == "0":
            break

        else:
            print("Opção inválida")


while True:

    print("\n=== SHOP GAMES ===")
    print("1 - Cadastrar usuário")
    print("2 - Login")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":

        nome = input("Digite seu nome: ")
        username = input("Digite seu username: ")
        senha = input("Digite sua senha: ")

        criar_usuario(nome, username, senha)

        print("Usuário cadastrado com sucesso!")

    elif opcao == "2":

        username = input("Digite seu username: ")
        senha = input("Digite sua senha: ")

        usuario = login_usuario(username, senha)

        if usuario:
            print("Login realizado com sucesso!")
            menu_loja(usuario)
        else:
            print("Dados incorretos")

    elif opcao == "0":
        break

    else:
        print("Opção inválida")