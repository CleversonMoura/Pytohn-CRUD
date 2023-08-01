# Importar as bibliotecas necessárias
from tkinter import *
from tkinter import ttk
import mysql.connector

# Configurar a conexão com o banco de dados MySQL
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='barbearia',
)

# Criar a janela principal da interface gráfica
janela = Tk()

# Função para inserir dados no banco de dados
def inserir_dados():
    # Pegar os valores das entradas dos campos
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()
    telefone = entry_telefone.get()

    # Verificar se todos os campos foram preenchidos
    if nome != "" and email != "" and senha != "" and telefone != "":

        # Verificar se os campos estão válidos
        if len(telefone) == 11 and len(senha) >= 8:
            try:
                # Criar um cursor para executar comandos SQL no banco de dados
                cursor = conexao.cursor()

                # Consulta SQL para verificar se o usuário já existe no banco de dados
                cmd = 'SELECT * FROM usuarios WHERE nome = %s OR email = %s'
                cursor.execute(cmd, (nome, email)) # Executar a consulta com parâmetros

                # Obter o resultado da consulta
                result = cursor.fetchall() # Ler o BD

                # Verificar se o usuário já está cadastrado
                if len(result) > 0:
                    print("[ERRO] Usuario ja cadastrado")
                else:
                    # Comando SQL para inserir os dados do novo usuário no banco de dados
                    cmd = 'INSERT INTO usuarios (nome, email, senha, telefone) VALUES (%s, %s, %s, %s)'
                    cursor.execute(cmd, (nome, email, senha, telefone)) # Executar o comando com parâmetros
                    conexao.commit() # Salvar as alterações no banco de dados
                    print("Usuario cadastrado")

                    # Limpar os campos após o cadastro
                    entry_nome.delete(0, END)
                    entry_email.delete(0, END)
                    entry_senha.delete(0, END)
                    entry_telefone.delete(0, END)

            except mysql.connector.Error as err:
                # Tratar erros ao executar comandos SQL
                print(f"[ERRO] Ocorreu um erro ao executar a consulta: {err}")
            finally:
                # Fechar o cursor após o uso
                cursor.close()
        else:
            print("[ERRO] O telefone ou a senha estão incorretos")
    else:
        print("[ERRO] Todos os campos devem estar preenchidos")

# Configuração da interface gráfica
janela.title("Cadastro de usuarios") # Título da janela

# Labels e Entradas (campos de texto) para coletar os dados do usuário
label_nome = ttk.Label(text="Nome")
label_email = ttk.Label(text="Email")
label_senha = ttk.Label(text="Senha")
label_telefone = ttk.Label(text="Telefone")

entry_nome = ttk.Entry() # Campo de texto para o nome
entry_email = ttk.Entry() # Campo de texto para o email
entry_senha = ttk.Entry() # Campo de texto para a senha
entry_telefone = ttk.Entry() # Campo de texto para o telefone

# Botão para cadastrar os dados no banco de dados
button_botao = ttk.Button(text="Cadastrar", command=inserir_dados)

# Posicionamento dos widgets na janela usando o sistema de grid
label_nome.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)
entry_nome.grid(row=1, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)
label_email.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)
entry_email.grid(row=2, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)
label_senha.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)
entry_senha.grid(row=3, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)
label_telefone.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)
entry_telefone.grid(row=4, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

button_botao.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

# Iniciar a execução da interface gráfica
janela.mainloop()
