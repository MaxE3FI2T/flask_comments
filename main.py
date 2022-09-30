from flask import render_template, Blueprint, request, url_for, redirect
from __init__ import create_app

bp_main = Blueprint('main', __name__)


@bp_main.route('/')
def index():
    return render_template('index.html')


@bp_main.route('/engraves')
def engraves():
    all_engraves = ""

    try:
        f = open('engraves.txt', 'r')
        f.seek(0)
        all_engraves = f.readlines()
        f.close()
    except:
        f = open('engraves.txt', 'x')
        f.close()

    return render_template('engraves.html', engraves=all_engraves)


@bp_main.route('/engraves', methods=['POST'])
def engraves_post():
    engrave = "\n" + request.form.get('txt')
    f = open('engraves.txt', 'a')
    f.writelines(engrave)
    f.close()

    return redirect(url_for('main.engraves'))

if __name__ == '__main__':
    create_app().run(debug=True, port=9876)
