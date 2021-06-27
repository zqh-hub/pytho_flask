from flask import Flask, render_template
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route("/filter")
def filter():
    # 过滤器：safe
    content = "<h1>不会转译</h1>"
    msg = "hello flask"
    lis_str = ["coco", "jojo", "gogo"]
    lis_int = [1, 2, 3, 0]
    return render_template("filter.html", content=content, msg=msg, lis_str=lis_str, lis_int=lis_int)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)
