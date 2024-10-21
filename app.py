from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Olá <br> Mundo!</h1>"

@app.route("/tiktok/<username>")
def aluno (username):
    return f'<h1>{username}</h1>'