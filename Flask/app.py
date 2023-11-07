from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def main_page():
    if(request.method == "POST"):
        contraseña=request.form.get('contraseña')
        usuario=request.form.get('usuario')
        pass
   
    return render_template("index.html")    
    


@app.route('/pruebaPost', methods=["POST","GET"]) 
def pruebaPost():
    if (request.method == "POST"):
        return "Esto es un POST"
    elif (request.method == "GET"):
        return "Estoy haciendo un get"
    return "Hola, esta es la web de baloncesto"


app.run()