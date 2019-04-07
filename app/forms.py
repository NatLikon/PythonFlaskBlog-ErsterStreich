from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
# wie du siehst, wird einiges von wtf-forms importiert

class CreatePost(FlaskForm):
    title = StringField('Titel', validators=[DataRequired()])
    body = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Abschicken')
    # die einzelnen Felder werden als Variablen angelegt