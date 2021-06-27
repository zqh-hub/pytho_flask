from flask import Flask, render_template
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route("/extend")
def extend():
    return render_template("extend.html")


@app.route("/include")
def include():
    return render_template("include.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)
