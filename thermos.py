from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)

bookmarks = []
app.config['SECRET_KEY'] = 'TC<\x02\xd8\x05\xfa7\xe47\xdf\xf7\xbe\x9c\xed\xebW\xd4\xff1*\x1b\xa87'

def store_bookmark(url):
    bookmarks.append(dict(
        url=url,
        user="muchai",
        date=datetime.utcnow()
    ))

def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True) [:num]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=new_bookmarks(5))

@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        url = request.form['url']
        store_bookmark(url)
        flash("Stored Bookmark '{}'".format(url))
        return redirect(url_for('index'))
    return render_template('add.html')

@app.errorhandler(404)
def page_not_found(event):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(event):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)
