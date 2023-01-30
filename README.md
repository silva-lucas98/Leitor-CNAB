# leitor-cnab

Aplicação para fazer upload arquivos CNAB, ler e interpretar dados, salvar no banco de dados e listar informações.

<br>

> Tecnologias utilizadas

- Python
- Django
- Django rest framework

<br>

> Como Executar Aplicação

* Faça clone desse repositório na máquina;

* Na pasta do projeto, execute o comando:

    * Criando Ambiente Virtual
        ```
        python -m venv venv
        ```

    * Ativando Ambiente Virtual
        ```
        source venv/bin/activate
        ```

    * Instalando Dependências
        ```
        pip install -r requirements.txt
        ```

* Executando Migrações

    ```
    python manage.py migrate
    ```

* Executando Aplicação

    ```
    python manage.py runserver
    ```

* Rotas da Aplicação

    * Upload de Arquivo:
        ```
        http://127.0.0.1:8000/api/
        ```

    * Listagem de Informações (direcionado automaticamente após upload):
        ```
        http://127.0.0.1:8000/api/list/
        ```