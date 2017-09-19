from datetime import datetime
from sqlalchemy import desc

try:
  from app import db
except ModuleNotFoundError:
  from thermos.thermos import BookmarkForm


class Bookmark(db.Model):
  __tablename__ = 'bookmark'

  id = db.Column(db.Integer, primary_key=True)
  url = db.Column(db.Text, nullable=False)
  date = db.Column(db.DateTime, default=datetime.utcnow)
  description = db.Column(db.String(300))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  @staticmethod
  def newest(num):
    return Bookmark.query.order_by(desc(Bookmark.date)).limit(num)


  def __repr__(self):
    return "<Bookmark '{}': '{}'>".format(self.description, self.url)

class User(db.Model):
  __tablename__ = 'user'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(100), unique=True)
  bookmarks = db.relationship('Bookmark', backref='user', lazy='dynamic')


  def __repr__(self):
    return '<User %r>' % self.username
