from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

"""
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                font: 16px sans-serif;
                border-radius: 10px;
            }

            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    """
form = """
    <form method="POST">
        <label for="rot">
        Rotate by:
        <input type="text" id="rot" name="rot" value="0"/>
        </label>
        <br><br>
        <textarea id="text" name="text">{0}</textarea>
        <br>
        <br>
        <button type="submit">Submit Query</button>
    </form>
    """
"""
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format('')
	
@app.route("/", methods=['POST'])
def encrypt():
    #do stuff with text & rot--convert data types as necessary ??
    text = request.form['text']
    rot = int(request.form['rot'])
    return form.format(rotate_string(text, rot))

app.run()