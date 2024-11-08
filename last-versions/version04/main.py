# importação dos modulos
from flask import Flask, render_template, jsonify

# comando basico do flask
app = Flask(__name__) 

# chat principal
@app.route("/")
def chat():
    return render_template("website.html")

@app.route("/adicionar_mensagem")
def adicionar_mensagem():
    from back_end import 
    return jsonify(tag='<p>Nova tag adicionada!</p>')


# só roda se for no programa principal
if __name__ == '__main__':
    app.run(debug = True, port=9744) 