from datetime import datetime
from flask import Flask, render_template, request

from logging import DEBUG

app = Flask(__name__)
app.logger.setLevel(DEBUG)

bookmarks = []

def store_bookmark(url):
    bookmarks.append(dict(
        url=url,
        user="muchai",
        date=datetime.utcnow()
    ))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Some new title", text=["Hey you", "again"])

@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        url = request.form['url']
        store_bookmark(url)
        app.logger.debug('stored url: ' + url)
    return render_template('add.html')

@app.errorhandler(404)
def page_not_found(event):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(event):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)
