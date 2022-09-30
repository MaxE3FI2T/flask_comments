from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'Qwertz1'

    from main import bp_main
    app.register_blueprint(bp_main)

    return app