import sqlite3


conexao = sqlite3.connect("SuperMarket.db")
banco = conexao.cursor()

sql = "create table Produto" \
      "(ID integer primary key,"\
      "CODIGO varchar(14),"\
      "DESCRICAO varchar(100),"\
      "PRECO_VENDA float,"\
      "PRECO_CUSTO float)"

banco.execute(sql)
conexao.commit()

