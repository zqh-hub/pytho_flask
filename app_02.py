from flask import Flask
import settings

app = Flask(__name__)
app.config.from_object(settings)  # 加载配置文件

# app.config.from_pyfile("settings.py")  # 第二种方式：它不用import settings了

'''
@app.route("/")
def main():
    return "hello world!"
'''


def index():
    return "<h1>Flask</h1>"


app.add_url_rule(rule="/index", view_func=index)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)
