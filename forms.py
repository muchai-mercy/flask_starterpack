from flask_wtf import Form
from wtforms.fields import StringField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url

class BookmarkForm(Form):
  url = URLField('url', validators=[DataRequired(), url()])
  description = StringField('description')
