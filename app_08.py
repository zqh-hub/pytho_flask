from flask import Flask, render_template, request, redirect, url_for
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route("/index", endpoint="home")  # endpoint:简单说是给这个路由起了一个别名，因为生产中，路由是很长的，这样比较方便
def index():
    return render_template("index.html")


@app.route("/register", endpoint="reg", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return redirect(url_for("home"))  # 反向找到/index
    return render_template("register.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)
