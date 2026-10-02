from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/nini2026")
def nini2026() :
    return render_template("ni1.html")

@app.route("/baptism")
def baptism() :
    return render_template("baptism.html")

if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=5000)