from flask import request, make_response, redirect, render_template, session, url_for, flash
import unittest #cada que se inicie hay que instalar --- pip install flask-testing
from app import create_app
from app.forms import LoginForm

app = create_app()


items = ["ITEM 1", "ITEM 2", "ITEM 3", "ITEM 4"]


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)
    

@app.errorhandler(404)
def not_found_endpint(error):
    return render_template('404.html', error=error)

@app.route('/index')
def index():
    user_dir = request.remote_addr
    response = make_response(redirect("/show_address_info")) #make-response mantiene los datos al redireccionar
    session["user_ip_info"] = user_dir
    return response
    
@app.route("/show_address_info", methods = ["GET", "POST"])
def show_info():
    user_ip = session.get("user_ip_info")
    username = session.get("username")
    login_form = LoginForm()
    context = {
        "user_ip":user_ip,
        "items":items,
        "login_form":login_form,
        "username":username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session["username"] = username
        flash("Nombre de usuario registrado correctamente")
        return redirect(url_for("index")) # url_for redirecciona sin datos previos (en blanco)

    return render_template("ip_info.html", **context)
    #**context simplemente desbarata el diccionario context y permite tomar las claves como variables


if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 3000, debug=True)