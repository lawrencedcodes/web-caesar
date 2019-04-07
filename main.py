from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True 
form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                font-weight: 600;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form method="post">
        <label>Rotate by:</label>
        <input name="rot" type="text" value="0">
        <textarea name="text"></textarea>
        <input type="submit" value="Submit">
      </form>
    </body>
</html>
"""

@app.route('/hello',methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return '<h1>Hello '+first_name+'</h1>'

@app.route('/',methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.text['text']
    return form
app.run()




