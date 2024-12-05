from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
<<<<<<< HEAD
    return "Hello Mar"        
=======
    return "Hello Mars"        
>>>>>>> 08f4cc9 (Desafio Custom Message)
