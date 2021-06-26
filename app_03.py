from flask import Flask
import settings

app = Flask(__name__)
app.config.from_object(settings)

data = {"a": "beijing", "b": "shanghai"}


@app.route("/get_city/<string:city_name_key>")
def get_city(city_name_key):
    return data.get(city_name_key)


@app.route("/get_sum/<int:num>")
def get_sum(num):
    sum = num + 10
    return str(sum)


@app.route("/get_two/<int:num1>/<int:num2>")
def two_num(num1, num2):
    return "num1={},num2={}".format(num1, num2)


@app.route("/get_path/<path:var_path>")
def get_path(var_path):
    return var_path


# c820d6fa-d5c3-11eb-9e4f-1e00ea11c771
@app.route("/get_uid/<uuid:uid>")  # http://localhost:9090/get_uid/c820d6fa-d5c3-11eb-9e4f-1e00ea11c771
def get_uid(uid):
    print(type(uid))
    return str(uid)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)
