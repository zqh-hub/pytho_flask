from flask import Flask
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route("/macro", methods=["GET", "POST"])
def macro():
    return "gg"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)
