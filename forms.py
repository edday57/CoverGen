from flask_wtf import Form, FlaskForm
from wtforms import Form, StringField


class SearchForm(Form):
    search = StringField('')
