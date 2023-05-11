# USE ESSE PROJETO

Clone esse repositório:
 - git clone https://github.com/ianroddrs/DEAC-PROJECT

Crie um virtual environment:
- py -m venv env 
- env\scripts\activate.bat

Instale as bibliotecas do projeto:
- pip install -r project/requirements.txt

Inicie o projeto:
- py manage.py runserver

<hr>

>### Para Adicionar novos arquivos estáticos
> 
>- py manage.py collectstatic 
>
>### Para adicionar novas bibliotecas ao requirements
>- py -m pip freeze > requirements.txt
