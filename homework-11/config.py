# -*- coding: utf-8 -*-

DEBUG = True
SECRET_KEY = 'This key must be secret!'
# WTF_CSRF_ENABLED = False

# Database settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

#Mail Settings
MAIL_SERVER = 'smtp.yandex.ru'
MAIL_PORT = 465
# MAIL_USE_TLS = default False
MAIL_USE_SSL = True
# MAIL_DEBUG = default app.debug
MAIL_USERNAME = 'flask.mail@yandex.ru'
MAIL_PASSWORD = 'qwerty1230'
# MAIL_DEFAULT_SENDER = default None
# MAIL_MAX_EMAILS = default None
# MAIL_SUPPRESS_SEND = default app.testing
# MAIL_ASCII_ATTACHMENTS = default False