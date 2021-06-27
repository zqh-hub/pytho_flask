##### python flask

###### 结构目录

```
项目名称：
	｜--- static(静态文件)
	｜--- templates(模版)
	｜--- app.py(运行)
web项目(MVC)：
	|--- model 模型
	|--- view 视图
  |--- controler 控制器
python(MTV):
	|--- model 模型
	|--- template 模版  html
	|--- view 视图 起控制作用 python代码
```

###### Run方法

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():  # 视图函数 mtv:view
    return 'Hello World! Hello Flask'

if __name__ == '__main__':
    # host:改为0.0.0.0外网可以访问
    # debug：True时，代码有改变就会重新加载代码
    app.run(host="0.0.0.0", port=9090, debug=True)
```

###### 通过config修改配置

```python
from flask import Flask

app = Flask(__name__)
print(app.config)
app.config["ENV"] = "development"  # 开发环境
app.config["DEBUG"] = True  # 开启debug模式

@app.route("/")
def index():
    return "我在学习flask"

if __name__ == '__main__':
    app.run(host="0.0.0.0")
```

###### 加载外部的settings配置文件

```python
from flask import Flask
import settings  # 导入配置文件

app = Flask(__name__)
app.config.from_object(settings)  # 加载配置文件
# app.config.from_pyfile("settings.py")  # 第二种方式：它不用import settings了

@app.route("/")
def index():
    return "hello world!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)
    
# settings.py
ENV = "development"
DEBUG = True
```

###### 解析@app.route()

```python
# route 源码：
# 我们会发现，这个注解里最重要的一句就是self.add_url_rule()
def route(self, rule: str, **options: t.Any) -> t.Callable:
  def decorator(f: t.Callable) -> t.Callable:
    endpoint = options.pop("endpoint", None)
    self.add_url_rule(rule, endpoint, f, **options)  # 调用的add_url_rule()
  	return f
return decorator
# add_url_rule源码：
@setupmethod
def add_url_rule(
  self,
  rule: str, # 这个参数没有默认值，是必填的
  endpoint: t.Optional[str] = None,
  view_func: t.Optional[t.Callable] = None, # 指定绑定哪个函数
  provide_automatic_options: t.Optional[bool] = None,
  **options: t.Any,
) -> None:
  raise NotImplementedError
 
# 不使用注解，自己写一个
from flask import Flask
import settings

app = Flask(__name__)
app.config.from_object(settings)

def index():
    return "<h1>Flask</h1>"

app.add_url_rule(rule="/index", view_func=index)  # 使用add_url_rule

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)
```

###### 路由变量规则

```python
from flask import Flask
import settings

app = Flask(__name__)
app.config.from_object(settings)

data = {"a": "北京", "b": "上海"}
@app.route("/get_city/<string:city_name_key>")   # http://localhost:9090/get_city/a --> 北京
def get_city(city_name_key):
    return data.get(city_name_key)

@app.route("/get_sum/<int:num>") # http://localhost:9090/get_sum/10 --> 20
def get_sum(num):
    sum = num + 10
    return str(sum)

@app.route("/get_two/<int:num1>/<int:num2>")  # 两个变量
def two_num(num1, num2):
    return "num1={},num2={}".format(num1, num2) 
  
@app.route("/get_path/<path:var_path>") # http://localhost:9090/get_path/sdsd/we --> sdsd/we
def get_path(var_path):
    return var_path

@app.route("/get_uid/<uuid:uid>")   # http://localhost:9090/get_uid/c820d6fa-d5c3-11eb-9e4f-1e00ea11c771  --> c820d6fa-d5c3-11eb-9e4f-1e00ea11c771
def get_uid(uid):
    print(type(uid))
    return str(uid)
 
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)
```

| 类型     | 描述                                |
| -------- | ----------------------------------- |
| * string | （缺省值） 接受任何不包含斜杠的文本 |
| * int    | 接受正整数                          |
| float    | 接受正浮点数                        |
| path     | 类似 `string` ，但可以包含斜杠      |
| uuid     | 接受 UUID 字符串                    |

###### 路由的唯一与重定向

```python
# 末尾有/,当你的浏览器访问的是https://xxx/projects时会重定向到https://xxx/projects/
@app.route('/projects/')
def projects():
    return 'The project page'

# 末尾没有/，会保持唯一。如果访问的是https://xxx/about/,会报Not found
@app.route('/about')
def about():
    return 'The about page'
```

###### 返回不同格式的content-type

```python
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
    return Response("python flask")  # 直接返回字符串其实再底层中将字符串封装成了Response

@app.route("/index4")
def return_tuple():
    return "sorry not found", 404   # 返回一个元组：内容,状态码
  
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)
```

###### response设置响应头

```python
from flask import Flask, make_response

import settings

app = Flask(__name__)
app.config.from_object(settings)

# 方式一：
@app.route("/index1")
response = Response("hello")
    response.headers["hhh"] = "flask"    # 设置响应头
    return response

# 方式二：make_response
@app.route("/index2")
def set_header():
    content = "hello flask "
    response = make_response(content)
    response.headers["my_header"] = "flask"   # 设置响应头
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)
```

###### 渲染模板

```python
# app.py
from flask import Flask, render_template   # 引入
import settings

app = Flask(__name__)
app.config.from_object(settings)

@app.route("/register")
def reg():
    template = render_template("register.html")    # 加载模板,之所以默认去template文件夹下找html，是因为在Flask初始化的时候指定了（template_folder: t.Optional[str] = "templates"）
    return template

if __name__ == '__main__':
    print(app.url_map)   # 路由规则表
    app.run(host="0.0.0.0", port=9090)

# template/register.html
<body>
<form action="" method="post">
    <label for="name">Name</label>
    <input type="text" name="name" id="name"><br>
    <label for="pwd"> Password </label>
    <input type="text" name="pwd" id="pwd"><br>
    <input type="submit" value="submit">
</form>
</body>
```

###### request处理get/post请求

```python
# app.py
from flask import Flask, render_template, request, Response
import settings

app = Flask(__name__)
app.config.from_object(settings)

@app.route("/register")
def reg():
    template = render_template("register.html")
    return template

@app.route("/index1", methods=["GET"])  # methods:指定能够接收的请求方式
def index1():
    print(request.args)  # 获取参数 ImmutableMultiDict([('name', 'coco'), ('pwd', '123')])
    print("name:", request.args.get("name"))  # coco
    print("password:", request.args.get("pwd"))
    return "首页"

@app.route("/index2", methods=["POST"])
def index2():
    print(request.form)   # 获取post请求参数
    print(request.form.get("name"))
    return "首页"

if __name__ == '__main__':
    print(app.url_map)
    app.run(host="0.0.0.0", port=9090)
    
# template/register.html
<body>
<form action="/index" method="get">
    <label for="name">Name</label>
    <input type="text" name="name" id="name"><br>
    <label for="pwd"> Password </label>
    <input type="text" name="pwd" id="pwd"><br>
    <input type="submit" value="submit">
</form>
</body>
```

###### 重定向

```python
import json

from flask import Flask, render_template, request, Response, redirect
import settings

app = Flask(__name__)
app.config.from_object(settings)
users = []

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":  # method:获取请求方式
        username = request.form.get("name")
        password = request.form.get("pwd")
        re_password = request.form.get("re_pwd")
        if re_password == password:
            user = {"username": username, "password": password}
            users.append(user)
            return redirect("/index") # 注册成功后，重定向到首页
        else:
            return "两次密码不一致"
    template = render_template("register.html")
    return template


@app.route("/show_users")
def show_users():
    data = json.dumps(users)
    return data


@app.route("/index")
def index():
    template = render_template("index.html")
    return template
```

![redirect_001](/Users/eric/Documents/python/python_code/python_flask/note/img/redirect_001.png)

###### url_for

```python
from flask import Flask, render_template, request, redirect, url_for
import settings

app = Flask(__name__)
app.config.from_object(settings)

@app.route("/index", endpoint="home")  # endpoint:简单说是给这个路由起了一个别名，因为生产中，路由是很长的，这样比较方便
def index():
    return render_template("index.html")

@app.route("/register", endpoint="reg", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return redirect(url_for("home"))  # 反向找到/index
    return render_template("register.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)
```

###### 模板取值

```python
# app.py
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
    friends = ["jojo", "gogo", "soso"]  # 列表
    likes = {"like1": "馍", "like2": "面条"}  # 字典
    tup = ("tuple_001", "tuple_002")
    mac = Mac("apple", "银色")  # 对象
    return render_template("show.html", name=name, age=age, friends=friends, likes=likes, tup=tup, mac=mac)

# template/show.html
<body>
<p>name:{{ name }}</p>
<p>age:{{ age }}</p>
<p>{{ friends.1 }}</p>
<p>{{ likes.like1 }}-----{{ likes.get("like1") }}</p>
<p>{{ tup.1 }}</p>
<p>{{ mac }}</p> # 默认调用__str__
<p> {{ mac.brand }} ----- {{ mac.color }}</p>
</body>
```

###### 模板注释

```python
# 模板引擎就不再去渲染它了
{# <p> {{ mac.brand }} ----- {{ mac.color }}</p> #}
```

###### 模板块

```python
<ul>   # for
    {% for friend in friends %}
        <li>{{ friend }}</li>
    {% endfor %}
</ul>
---- ---- ---- ---- ---- ---- ---- ---- ---- 
<ul>  # if -- else
    {% for friend in friends %}
        {% if friend | length>2 %}
            <li style="color: cadetblue">{{ friend }}</li>
        {% else %}
            <li>{{ friend }}</li>
        {% endif %}

    {% endfor %}
</ul>
</body>
---- ---- ---- ---- ---- ---- ---- ---- ---- 
users = [
        {"name": "123", "age": 12, "friends": ["coco", "soso"]},
        {"name": "123", "age": 12, "friends": ["coco", "soso"]},
        {"name": "123", "age": 12, "friends": ["coco", "soso"]}
    ]

<table>
    {% for user in users %}
        <tr>
            <td>{{ user.name }}</td>
            <td>{{ user.age }}</td>
            <td>{{ user.friends }}</td>
            <td>{{ user.friends.1 }}</td>
        </tr>
    {% endfor %}
</table>
```

###### loop

```python
<table>
    {% for user in users %}
        <tr>
            <td>{{ loop.index0 }}</td>  {# index,reindex,index0,reindex0 #}
            <td>{{ loop.first }}</td>   {# first:判断是否是第一行;last:判断是否是最后一行 #}

            <td>{{ user.name }}</td>
            <td>{{ user.age }}</td>
            <td>{{ user.friends }}</td>
            <td>{{ user.friends.1 }}</td>
        </tr>
    {% endfor %}
</table>
```

###### 过滤器

```
# app.py
@app.route("/filter")
def filter():
    content = "<h1>不会转译</h1>"
    msg = "hello flask"
    lis_str = ["coco", "jojo", "gogo"]
    lis_int = [1, 2, 3, 0]
    return render_template("filter.html", content=content, msg=msg, lis_str=lis_str, lis_int=lis_int)
# 字符串常见过滤器：
<body>
{{ content | safe }}  {# 禁止转译 #}
{{ msg | upper }}  {# upper:大写；lower：小写 #}
{{ msg | capitalize }}  {# 首字母大写 #}
{{ msg | title }}  {# 每句话的每个单词的首字母大写 #}
{{ msg | reverse }}  {# 翻转 #}
{{ "%s" | format(msg) }}  {# 格式化 #}
{{ msg | truncate(4) }}  {# truncate会返回一个被阶段性的字符串#}
</body>

# 列表常见过滤器
{{ lis_str | length }} {# 长度 #}
{{ lis_str | first }} {# 第一个值 #}
{{ lis_str | last }} {# 最后一个值 #}
{{ lis_int | sum }} {# 求和 #}
{{ lis_int | sort }} {# 排序 #}
```

###### 读取字典

```python
#app.py
@app.route("/dic")
def dic_temp():
    users = [
        {"name": "123", "age": 12, "friends": ["coco", "soso"]},
        {"name": "123", "age": 12, "friends": ["coco", "soso"]},
        {"name": "123", "age": 12, "friends": ["coco", "soso"]}
    ]
    return render_template("dic.html", users=users)
    
# template/dic.html
<body>
{% for v in users.0.values() %}    {# values #}
    <p>{{ v }}</p>
{% endfor %}

{% for k in users.0.keys() %}   {# keys #}
    <p>{{ k }}</p>
{% endfor %}
  
{% for k,v in users.0.items() %}   {# items #}
    <p>{{ k }}-----{{ v }}</p>
{% endfor %}
</body>
```

###### 自定义过滤器

```python
#app.py
from flask import Flask, render_template
import settings

app = Flask(__name__)
app.config.from_object(settings)

@app.route("/customize_filter")
def customize_filter():
    msg = "hello world"
    lis = [1, 2, 3]
    return render_template("customize_filter.html", msg=msg, lis=lis)


# 方式1：通过函数
def add_filter_by_fun(old, new):
    rep = old.replace("world", new)
    return rep  # 一定要返回值

app.add_template_filter(add_filter_by_fun, "filter_by_fun")


# 方式2：通过注解
@app.template_filter("filter_by_annot")
def add_filter_by_annot(old, new):
    rep = old.replace("world", new)
    return rep  # 一定要返回值
    
# template/customize_filter.html
<body>
{{ msg | filter_by_fun(new = "flask") }}
{{ msg | filter_by_annot(new = "flask") }}
</body>
```

###### 模板继承extend

```python
# base.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}基础page的title{% endblock %}</title>
    <style>
        #nav {
            background-color: cadetblue;
        }

        #top {
            background-color: darkolivegreen;
        }

        #middle {
            height: 500px;
            background-color: darkslategrey;
        }

        #foot {
            background-color: darkolivegreen;
        }
    </style>
    {% block my_css %}{% endblock %}
</head>
<body>
<div id="nav">导航栏</div>
<div id="top">头部</div>
<div id="middle">
    {% block middle %}中间内容{% endblock %}
</div>
<div id="foot">底部</div>
{% block script %}

{% endblock %}
</body>
</html>

# extend.html
{% extends "base.html" %}      {# 继承 base page #}
{% block title %}         {# title #}
    extend
{% endblock %}

{% block my_css %}         {# css #}
    <style>
        #middle {
            background-color: cadetblue;
        }
    </style>
  	{# 引进外部css #}
		<link rel="stylesheet" href="{{ url_for("static",filename="css/my_css.css") }}">
{% endblock %}
{% block middle %}           {# middle #}
    <button id="btn">点我</button>
{% endblock %}
{% block script %}            {# script #}
    <script>
        btn = document.getElementById("btn")
        btn.onclick = function () {
            alert("你竟然点我")
        }
    </script>
{% endblock %}
```

###### 模板导入include

```python
# template/common/header.html
<div style="background-color: darkolivegreen">
    我是头部
</div>

# template/include.html
<body>
{% include  "common/header.html" %}       {# include #}
<h3>这里是include</h3>
</body>
```

###### 模板的宏

```python
# template/common/macro.html
{# 这里把所有的宏单独写出来 #}
{% macro form(action,method="POST",value="登录") %}
    <form action="{{ action }}" method="{{ method }}">
        Username:<input type="text" name="username">
        Password:<input type="text" name="password">
        <input type="submit" value="{{ value }}">
    </form>
{% endmacro %}

# template/macro1.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>宏</title>
</head>
<body>
{# 宏其实就是定一个函数,可以写在内部，也可以在外部   - - - - - - - - - - - - - - 将宏定义在内部
{% macro form(action,method="POST",value="登录") %}
    <form action="{{ action }}" method="{{ method }}">
        Username:<input type="text" name="username">
        Password:<input type="text" name="password">
        <input type="submit" value="{{ value }}">
    </form>
{% endmacro %}
#}

{# 使用内部的宏
{{ form(action="/macro") }} #}   - - - - - - - - - - - - - - 使用内部的宏

{# 引入外部的宏 #}
{% import "common/macro.html" as ro %}   - - - - - - - - - - - - - - 使用外部的宏
{{ ro.form(action="/macro",value="提交") }}
</body>
</html>
```

###### 模板中的变量

```
# 全局变量
{% set username="jojo" %}    
{{ username }}     -------使用
# 局部变量
with -------
```

