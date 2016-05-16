from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length

class EditForm(Form):
    texto1 = StringField ('texto1', validators=[DataRequired()])
    texto2 = TextAreaField('texto2', validators=[Length(min=0, max=140)])
