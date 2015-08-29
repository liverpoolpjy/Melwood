# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from flask.ext.pagedown.fields import PageDownField
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import Required, Length, Email, Regexp, URL
from wtforms import ValidationError
from ..models import Post, Comment


class PostForm(Form):
    title = StringField('Title', validators=[Required()])
    body = PageDownField('Body', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(Form):
    author_name = StringField('Your name', validators=[Required(), Length(1, 64)])
    author_email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    author_website = StringField('Your website', validators=[Length(0, 64)])
    body = PageDownField('Enter your comment (Markdown)', validators=[Required()])
    submit = SubmitField('Submit')