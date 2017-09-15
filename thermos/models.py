from datetime import datetime

from thermos.thermos import db

class Bookmark(db.Model):
  __tablename__ = 'bookmark'

  id = db.Column(db.Integer, primary_key=True)
  url = db.Column(db.Text, nullable=False)
  date = db.Column(db.DateTime, default=datetime.utcnow)
  description = db.Column(db.String(300))

  def __repr__(self):
    return "<Bookmark '{}': '{}'>".format(self.description, self.url)

class User(db.Model):
  __tablename__ = 'user'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(100), unique=True)


  def __repr__(self):
    return '<User %r>' % self.username
