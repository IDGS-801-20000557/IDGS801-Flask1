from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "<h1 style='color: red; text-align: center;'>Hola Mundo Flask cambios nuevos</h1>"

@app.route("/Hola")
def hola():
    return "hola BB"

@app.route("/nueva")
def nueva():
    return "hola desde nueva"

if __name__=="__main__":
    app.run(debug=True, port=3000)

