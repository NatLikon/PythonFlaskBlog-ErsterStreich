from app import app, db
from flask import flash, redirect, render_template, url_for
from app.forms import CreatePost
from app.models import Post


@app.route('/')
@app.route('/index')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/createpost', methods=['GET', 'POST'])
def createpost():
    form = CreatePost()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data)
        db.session.add(post)
        db.session.commit()
        flash('Post angelegt!')
        return redirect(url_for('createpost'))

    return render_template('createpost.html', title='Einen Artikel schreiben', form=form)