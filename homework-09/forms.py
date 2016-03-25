# -*- coding: utf-8 -*-

from models import *
from wtforms_alchemy import ModelForm

# https://wtforms-alchemy.readthedocs.org/en/latest/introduction.html
# http://wtforms-alchemy.readthedocs.org/en/latest/configuration.html#modelform-meta-parameters


class PostForm(ModelForm):
    class Meta:
        model = Post
        only = ['title', 'text']
