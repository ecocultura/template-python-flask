from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap = Bootstrap(app)
app.config["SECRET_KEY"] = 'CLAVE SEGURA'


items = ["ITEM 1", "ITEM 2", "ITEM 3", "ITEM 4"]

@app.errorhandler(404)
def not_found_endpint(error):
    return render_template('404.html', error=error)

@app.route('/index')
def index():
    user_dir = request.remote_addr
    response = make_response(redirect("/show_address_info"))
    session["user_ip_info"] = user_dir
    return response
    
@app.route("/show_address_info")
def show_info():
    user_ip = session.get("user_ip_info")
    context = {
        "user_ip":user_ip,
        "items":items
    }
    return render_template("ip_info.html", **context)
    #**context simplemente desbarata el diccionario context y permite tomar las claves como variables


if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 3000, debug=True)