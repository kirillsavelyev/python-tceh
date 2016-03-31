# -*- coding: utf-8 -*-

from flask import (
    Blueprint,
    redirect,
    url_for,
    flash,
    request,
    render_template
)
from flask.ext.login import login_required, current_user
from flask_mail import Message
from forms import PostForm, BackwardForm
from models import User, Post
from app import db, mail

blog = Blueprint('blog', __name__)
# admin = Blueprint('admin', __name__, url_prefix='/admin')
# https://github.com/apiguy/flask-classy


# Views:


@blog.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        user = User.query.filter_by(username=current_user.username).first()
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


@blog.route('/delete_post', methods=['POST'])
@login_required
def delete_post():
    if request.method == 'POST':
        post_id = request.form['id']
        post = Post.query.filter_by(id=post_id).first()
        post.is_visible = False
        db.session.commit()
        flash('Post {} deleted!'.format(post_id))
        # form = PostForm()
        # posts = Post.query.filter_by(is_visible=True).all()
        # return render_template('home.html', form=form, posts=posts)
        return redirect(url_for('blog.home'))


@blog.route('/user_profile', methods=['GET', 'POST'])
@login_required
def user_profile():
    if request.method == 'GET':
        return render_template('user_profile.html', form=BackwardForm())

    if request.method == 'POST':
        form = BackwardForm(request.form)
        if form.validate():
            msg = Message(
                form.title.data,
                sender=[current_user.username, 'flask.mail@yandex.ru'],
                recipients=['flask.mail@yandex.ru']
            )
            msg.body = form.text.data
            mail.send(msg)

            flash('Message will be send!')

        return redirect(url_for('blog.user_profile'))
