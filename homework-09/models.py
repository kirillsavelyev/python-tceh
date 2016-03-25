# -*- coding: utf-8 -*-

import datetime

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

    def __str__(self):
        return repr(self)

    # TODO: Поискать методы отобажения названий полей в фоме ввода

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(
        'User', backref=db.backref('posts', lazy='dynamic'))
    title = db.Column(db.String(150), unique=True)
    text = db.Column(db.String(3500))
    date = db.Column(db.Date, default=datetime.date.today())
    is_visible = db.Column(db.Boolean, default=True)

    def __init__(self, user=None, title='', text='',
                 date=None, is_visible=None):
        self.user = user
        self.title = title
        self.text = text
        self.date = date
        self.is_visible = is_visible
