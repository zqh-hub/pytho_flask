from flask import Flask, render_template
import settings

app = Flask(__name__)
app.config.from_object(settings)


class Mac:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __str__(self):
        return self.brand

    def get_color(self):
        return self.color


@app.route("/show")
def show():
    name = "coco"  # 字符串
    age = 24  # 数字
    friends = ["jojo", "gogo", "so"]  # 列表
    likes = {"like1": "馍", "like2": "面条"}  # 字典
    tup = ("tuple_001", "tuple_002")
    mac = Mac("apple", "银色")  # 对象
    users = [
        {"name": "123", "age": 12, "friends": ["coco", "soso"]},
        {"name": "123", "age": 12, "friends": ["coco", "soso"]},
        {"name": "123", "age": 12, "friends": ["coco", "soso"]}
    ]
    return render_template("show.html", name=name, age=age, friends=friends, likes=likes, tup=tup, mac=mac, users=users)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)
