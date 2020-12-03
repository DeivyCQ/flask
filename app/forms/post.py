from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    post = TextAreaField('Mensaje', validators=[DataRequired(), Length(min=1, max=200)])
    submit = SubmitField('Conectarse')