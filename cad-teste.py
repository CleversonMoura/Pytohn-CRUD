from tkinter import *
from tkinter import ttk

user = []

janela = Tk()

#criar a função de pegar os valores
def inserir_dados():
    #pega os valores das entradas
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()
    telefone = entry_telefone.get()
    #verifica se nao estao vazios
    if nome != "" and email != "" and senha != "" and telefone != "":
        #verifica se os campos estao validos
        if len(telefone) == 11 and len(senha) >= 8:
            user.append((nome,email,senha,telefone))
            print(user)
        else:
            print("[ERRO] O telefone ou a senha estão incorretos")
    else:
        print("[ERRO] Todos os campos devem estar preenchidos")
    

#titulo
janela.title("Cadastro de usuarios")

label_nome = ttk.Label(text="Nome")
label_email = ttk.Label(text="Email")
label_senha = ttk.Label(text="Senha")
label_telefone = ttk.Label(text="Telefone")

entry_nome = ttk.Entry()
entry_email = ttk.Entry()
entry_senha = ttk.Entry()
entry_telefone = ttk.Entry()

button_botao = ttk.Button(text="Cadastrar", command=inserir_dados)

label_nome.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)
entry_nome.grid(row=1, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)
label_email.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)
entry_email.grid(row=2, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)
label_senha.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)
entry_senha.grid(row=3, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)
label_telefone.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)
entry_telefone.grid(row=4, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

button_botao.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)


janela.mainloop()
