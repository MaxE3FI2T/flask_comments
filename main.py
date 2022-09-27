from flask import Flask, render_template

app = Flask(__name__)


# STRG + Alt + L Auto Formatter
@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True, port=9876)
