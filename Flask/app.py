from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def hola():
    user = ""
    password = ""
    if (request.method == "POST"):
        user = request.form.get("usuario")
        password = request.form.get("contraseña")
        print(user, password)
    return render_template("index.html", user=user, password=password)

@app.route("/baloncesto")
def baloncesto():
    return "Hola, esta es la web de baloncesto!"

@app.route("/pruebaPost", methods=["POST","GET"])
def pruebaPost():
    if (request.method == "POST"):
        return "Esto es un POST"
    elif (request.method == "GET"):
        return "Esto es un GET"
    return "Hola, esta es la web de baloncesto!"

app.run()