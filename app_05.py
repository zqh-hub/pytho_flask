from flask import Flask, make_response

import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route("/index")
def set_header():
    content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        div {
            background-color:cadetblue;
            width: 100%;
            height: 200px;
        }
    </style>
</head>
<body>
<div> hello flask</div>
</body>
</html>
'''
    response = make_response(content)
    response.headers["my_header"] = "flask"
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)
