from flask import Flask, render_template
app = Flask(__name__)

filmes = [
    "título: 10 Coisas que eu odeio em você",
    "título: Meninas Malvadas",
    "título: De repente, 30",
    "título: Operação Cupido",
    "título: As Patricinhas de Beverly Hills",
    "título: Diário da Princesa",
    "título: 17 Outra Vez",
    "título: A Nova Cinderela"
]
@app.route('/')
def lista_filmes():
    return render_template('index.html', lista_filmes=filmes)

if __name__ == '__main__':
    app.run(debug=True)