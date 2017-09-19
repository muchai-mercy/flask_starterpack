import os
from datetime import datetime
from flask import render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from app import app, db
import models
try:
    from models import Bookmark, User
    from forms import BookmarkForm
except ModuleNotFoundError:
    from thermos.forms import BookmarkForm

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
environment = os.getenv("FLASK_CONFIG")

bookmarks = []
app.config['SECRET_KEY'] = 'TC<\x02\xd8\x05\xfa7\xe47\xdf\xf7\xbe\x9c\xed\xebW\xd4\xff1*\x1b\xa87'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'thermos.db')

def store_bookmark(url):
    bookmarks.append(dict(
        url=url,
        user="muchai",
        date=datetime.utcnow()
    ))

# def new_bookmarks(num):
#     return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True) [:num]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=models.Bookmark.newest(5))

@app.route('/add', methods=["GET", "POST"])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        user_id = form.user_id.data
        bm = models.Bookmark(url=url, description=description)
        db.session.add(bm)
        db.session.commit()
        store_bookmark(description)
        flash("Stored '{}'".format(description))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.errorhandler(404)
def page_not_found(event):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(event):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)
