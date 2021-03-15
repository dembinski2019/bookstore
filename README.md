# BookStore

Api para Sistema de Biblioteca.

Projeto desenvolvido para concorrer a vaga de desenvolvedor backend python Jr na Agriness

Para ver em funcionamento no heroku clique [aqui]().



## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com Python 3.8
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instancia com o .env
6. Execute os testes.
7. Execute o sitema localmente.
8. Abra em seu navegador e verá a docuemntação eletronica..

```console
git clone git@github.com/dembinski2019/bookstore.git bookstore
cd bookstore
python -m venv .venv
source .venv/bim/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
python manage.py runserver
localhost:8000 
```
## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Define uma SECRET_KEY segura para instância.
4. Defina DEBUG=False
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set "SECRET_KEY=`python contrib/secret_gen.py`"
heroku config:set "DEBUG=False"
git push heroku master --force
```
