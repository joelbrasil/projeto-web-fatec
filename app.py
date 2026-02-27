# Importa Flask e também a função render_template
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def pagina_inicial():
    # render_template busca o arquivo na pasta templates/
    # e retorna seu conteúdo como resposta HTTP
    return render_template('index.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/bootstraps')
def bootstrap():
    return render_template('bootstraps.html')


if __name__ == '__main__':
    app.run(debug=True)