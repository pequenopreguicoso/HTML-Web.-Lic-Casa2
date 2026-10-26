from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

fatos = [
    "Os polvos possuem três corações!",
    "O mel pode durar milhares de anos se for armazenado corretamente.",
    "Os tubarões existem há mais tempo que as árvores.",
    "Um dia em Vênus dura mais que um ano em Vênus.",
    "As borboletas sentem sabores com os pés.",
    "Os golfinhos utilizam assobios individuais para se identificar.",
    "A Torre Eiffel pode ficar mais alta durante o verão por causa do calor.",
    "Os coalas possuem impressões digitais muito parecidas com as humanas.",
    "A luz do Sol leva aproximadamente 8 minutos para chegar à Terra.",
    "O coração de uma baleia-azul pode pesar mais de 150 kg."
]

@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/fato")
def gerar_fato():
    fato = random.choice(fatos)
    return jsonify({"fato": fato})

@app.route("/secret")
def pagina_secreta():
    resultado = random.choice(["🪙 Cara!", "🪙 Coroa!"])

    return f"""
    <html>
    <head>
        <title>Página Secreta</title>
    </head>
    <body style="background-color: #141e30; color: white;
                 text-align: center; font-family: Arial; padding: 80px;">

        <h1>🔐 Você encontrou a página secreta!</h1>

        <h2>{resultado}</h2>

        <p>Clique no botão para jogar novamente!</p>

        <button onclick="location.reload()"
                style="padding: 15px; font-size: 18px; cursor: pointer;">
            🪙 Jogar novamente
        </button>

        <br><br>

        <a href="/" style="color: #00c9a7;">
            Voltar ao início
        </a>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)