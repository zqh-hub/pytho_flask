from flask import Flask, render_template,request
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route("/macro", methods=["GET", "POST"])
def macro():
    if request.method == "POST":
        return "index"
    return render_template("macro.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)
