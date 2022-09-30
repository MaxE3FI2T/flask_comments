from flask import render_template, Blueprint
from __init__ import create_app

bp_main = Blueprint('main', __name__)


@bp_main.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    create_app().run(debug=True, port=9876)