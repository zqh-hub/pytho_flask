from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # 视图函数 mtv:view
    return 'Hello World! Hello Flask'


if __name__ == '__main__':
    # host:改为0.0.0.0外网可以访问
    # debug：True时，代码有改变就会重新加载代码
    app.run(host="0.0.0.0", port=9090, debug=True)
