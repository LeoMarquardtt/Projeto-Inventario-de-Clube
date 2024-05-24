import sqlite3 as lite

#conexao
con = lite.connect('dados.db')

#tabela
with con:
    cur=con.cursor()
    cur.execute('CREATE TABLE inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, posicao TEXT, numero TEXT, lugar_nasc TEXT, data_da_compra DATE, fim_ctt DATE, valor_da_compra DECIMAL, imagem)')