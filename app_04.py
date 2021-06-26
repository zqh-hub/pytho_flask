from flask import Flask, Response

import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route("/index1")
def return_string():
    return "hello flask"  # Content-Type: text/html; charset=utf-8


@app.route("/index2")
def return_dict():
    return {"a": "beijing", "b": 123, "c": [123, 43]}  # Content-Type: application/json


@app.route("/index3")
def return_response():
    # return Response("hello flask")  # 直接返回字符串其实再底层中将字符串封装成了Response
    response = Response("hello")
    response.headers["hhh"] = "flask"
    return response


@app.route("/index4")
def return_tuple():
    return "sorry not found", 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)
