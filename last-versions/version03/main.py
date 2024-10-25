# importação dos modulos
from flask import Flask, render_template, url_for

# comando basico do flask
app = Flask(__name__) 

# chat principal
@app.route("/")
def chat():
    return render_template("website.html")

# só roda se for no programa principal
if __name__ == '__main__':
    app.run(debug = True, port=9744) 