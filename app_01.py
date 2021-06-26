from flask import Flask

app = Flask(__name__)
print(app.config)
app.config["ENV"] = "development"
app.config["DEBUG"] = True


@app.route("/")
def index():
    return "我在学习flask"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
