from flask import Flask, render_template
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route("/customize_filter")
def customize_filter():
    msg = "hello world"
    lis = [1, 2, 3]
    return render_template("customize_filter.html", msg=msg, lis=lis)


# 方式1：
def add_filter_by_fun(old, new):
    rep = old.replace("world", new)
    return rep  # 一定要返回值


app.add_template_filter(add_filter_by_fun, "filter_by_fun")


# 方式2：
@app.template_filter("filter_by_annot")
def add_filter_by_annot(old, new):
    rep = old.replace("world", new)
    return rep  # 一定要返回值


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)
