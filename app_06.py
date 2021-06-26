from flask import Flask, render_template, request, Response
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route("/register", methods=["GET"])
def reg():
    template = render_template("register.html")
    return template


@app.route("/index", )
def index():
    print(request.args)
    print("name:", request.args.get("name"))
    print("password:", request.args.get("pwd"))
    return "首页"


if __name__ == '__main__':
    print(app.url_map)
    app.run(host="0.0.0.0", port=9090)
