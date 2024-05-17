from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    user_dir = request.remote_addr
    response = make_response(redirect("/show_address_info"))
    response.set_cookie("user_ip_info", user_dir)
    return response
    
@app.route("/show_address_info")
def show_info():
    user_ip = request.cookies.get("user_ip_info")
    return render_template("ip_info.html", user_ip=user_ip)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 3000, debug=True)