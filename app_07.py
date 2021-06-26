import json

from flask import Flask, render_template, request, Response
import settings

app = Flask(__name__)
app.config.from_object(settings)
users = []


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("name")
        password = request.form.get("pwd")
        re_password = request.form.get("re_pwd")
        if re_password == password:
            user = {"username": username, "password": password}
            users.append(user)
            return "注册成功"
        else:
            return "两次密码不一致"
    template = render_template("register.html")
    return template


@app.route("/show_users")
def show_users():
    data = json.dumps(users)
    return data


if __name__ == '__main__':
    print(app.url_map)
    app.run(host="0.0.0.0", port=9090)
