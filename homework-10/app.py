# -*- coding: utf-8 -*-

import config

from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask_mail import Mail


login_manager = LoginManager()
db = SQLAlchemy()
mail = Mail()


def create_app():
    from views import blog
    from auth import auth

    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config)

    app.register_blueprint(auth)
    app.register_blueprint(blog)

    login_manager.init_app(app)

    mail.init_app(app)
    db.init_app(app)

    # Dynamic context:
    with app.app_context():
        db.create_all()

    return app


@login_manager.user_loader
def load_user(user_id):
    from models import User

    return User.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.login'))
    # return 'Unauthorized', 401


if __name__ == '__main__':
    app = create_app()
    app.run()

    # from models import *
    # db.create_all()
    # user = User(username='SKA', email='ska@yandex.ru')
    # db.session.add(user)
    # db.session.commit()

    # TODO:  добавить егистацию и автоизацию
