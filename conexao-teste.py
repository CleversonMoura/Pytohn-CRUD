import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='barbearia',
)

cursor = conexao.cursor()

nome = "Tony Tony"
email = "tonyim@gmail.com"
senha = "abc12345"
telefone = "88993003307"


cmd = f'SELECT * FROM `usuarios` WHERE nome = "{nome}" OR email = "{email}"'
cursor.execute(cmd) # executar o comando
result = cursor.fetchall() # ler o BD
# verificar se o usuario ja existe
if len(result) > 0:
    print("[ERRO] Usuario ja cadastrado")
else:
    cmd = f'INSERT INTO usuarios (nome, email, senha, telefone) VALUES ( "{nome}", "{email}" ,"{senha}" ,"{telefone}" )'
    cursor.execute(cmd) # executar o comando
    conexao.commit() # para edita o BD
    print("Usuario cadastrado")


cursor.close()
conexao.close()