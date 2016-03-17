# -*- coding: utf-8 -*-

from wtforms import StringField, validators, ValidationError, Form

# def full_name_validator(form, field):
#     name_parts = field.data.split(' ')
#     if len(name_parts) < 2:
#         raise ValidationError('Name is not full!')


class ContactForm(Form):
    name = StringField(label='Name', validators=[
        validators.Length(min=2, max=50),
        # , full_name_validator
    ])
    title = StringField(label='Title', validators=[
        validators.Length(min=4, max=100)
    ])
    text = StringField(label='Text', validators=[
        validators.Length(min=6, max=3500)
    ])


