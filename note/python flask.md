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

