# -*- coding: utf-8 -*-
from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from .forms import PostForm, CommentForm
from . import main 
from .. import db
from ..models import Post, Comment

@main.route('/', methods=['GET', 'POST'])
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', posts=posts) 

@main.route('/update', methods=['GET', 'POST'])
def update():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,
            body=form.body.data)
        db.session.add(post)
        return redirect(url_for('.index'))
    return render_template('update.html', form=form)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/archive')
def archive():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('archive.html',posts=posts)

@main.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    post = Post.query.get_or_404(id)
    return render_template('post.html', post=post)

@main.route('/edit_post/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    post = Post.query.get_or_404(id)
    form = PostForm()
    if form.validate_on_submit():
        # post = Post(title=form.title.data,
        #     body=form.body.data)
        post.body = form.body.data
        post.title = form.title.data
        db.session.add(post)
        flash('The post has been updated.')
        return redirect(url_for('.post', id=post.id))
    form.title.data = post.title
    form.body.data = post.body
    return render_template('update.html', form=form)

@main.route('/delete/<int:id>')
def delete(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    flash('The post has been deleted.')
    return redirect(url_for('.archive'))
    