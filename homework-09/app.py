# -*- coding: utf-8 -*-

import config
# from flask.ext.qrcode import QRcode

from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from wtforms.ext.sqlalchemy.orm import model_form


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    from models import Post, User
    from forms import PostForm

    if request.method == 'POST':
        user = User.query.filter_by(username='SKA').first()
        form = PostForm(request.form)
        if form.validate():
            form.user = user
            post = Post(user=user, **form.data)
            db.session.add(post)
            db.session.commit()

    form = PostForm()

    visible_posts = Post.query.filter_by(is_visible=True).all()
    return render_template(
        'home.html', form=form, posts=visible_posts)


@app.route('/delete_post', methods=['POST'])
def delete_post():
    from models import Post
    # from forms import PostForm
    # post_form_class = model_form(Post, base_class=Form, db_session=db.session)
    # form = post_form_class(request.form)

    if request.method == 'POST':
        post_id = request.form['id']
        post = Post.query.filter_by(id=post_id).first()
        post.is_visible = False
        db.session.commit()
        flash('Post {} deleted!'.format(post_id))
        # form = PostForm()
        # posts = Post.query.filter_by(is_visible=True).all()
        # return render_template('home.html', form=form, posts=posts)
        return redirect(url_for('home'))


if __name__ == '__main__':
    from models import *
    db.create_all()
    # user = User(username='SKA', email='ska@yandex.ru')
    # db.session.add(user)
    # db.session.commit()
    app.run()

    # TODO:  добавить егистацию и автоизацию
