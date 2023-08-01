# Cadastro de Usuários - Aplicativo com Tkinter e MySQL

Este é um simples aplicativo de cadastro de usuários criado em Python utilizando a biblioteca Tkinter para a interface gráfica e o banco de dados MySQL para armazenar os dados dos usuários.

## Funcionalidades

- Cadastro de novos usuários com nome, e-mail, senha e telefone.
- Verificação de duplicatas: o sistema impede que usuários com o mesmo nome ou e-mail sejam cadastrados novamente.
- Validação de campos: o telefone deve conter exatamente 11 dígitos e a senha deve ter pelo menos 8 caracteres.

## Requisitos

- Python 3.x
- Bibliotecas: `tkinter`, `mysql-connector-python`

## Instalação

1. Certifique-se de ter o Python 3.x instalado em seu sistema.
2. Instale as dependências necessárias usando o gerenciador de pacotes `pip`:

```
pip install mysql-connector-python
```

## Como executar

1. Clone este repositório para o seu computador ou faça o download dos arquivos.
2. Abra o terminal ou prompt de comando e navegue até o diretório do projeto.
3. Execute o arquivo `cadastro_usuarios.py`:

```
python cadastro_usuarios.py
```

## Uso

1. Preencha os campos de nome, e-mail, senha e telefone.
2. Clique no botão "Cadastrar" para salvar os dados no banco de dados.
3. Os campos serão limpos após o cadastro bem-sucedido.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções para este projeto. Se você encontrar algum problema, por favor, abra uma "Issue" no repositório.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
