import psycopg2
import csv

# Conecta-se ao banco de dados
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="destrux2792"
)

# Cria um cursor para executar comandos SQL
cur = conn.cursor()

# Limpa a tabela antes de inserir novos dados
cur.execute("TRUNCATE books")

# Abre o arquivo CSV
with open('arquivos/dados.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        # Insere os dados na tabela
        cur.execute(
            "INSERT INTO books (nome, categoria, nota, upc, tipo, preco_sem_taxa, preco_com_taxa, taxa, estoque, num_reviews) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            row
        )

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão com o banco de dados
cur.close()
conn.close()