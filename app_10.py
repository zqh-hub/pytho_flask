from flask import Flask, render_template
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route("/show02")
def show02():
    users = [
        {"name": "123", "age": 12, "friends": ["coco", "soso"]},
        {"name": "123", "age": 12, "friends": ["coco", "soso"]},
        {"name": "123", "age": 12, "friends": ["coco", "soso"]}
    ]
    return render_template("show_02.html", users=users)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)
