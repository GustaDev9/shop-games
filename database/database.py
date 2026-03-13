#criando o banco de dados mysql sem api

import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Tocada2009@",
        database="shop_games"
    )
    
    return conexao

