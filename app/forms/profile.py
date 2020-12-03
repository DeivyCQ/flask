from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class ProfileForm(FlaskForm):
    post = StringField('Usuario', validators=[DataRequired()])
    about_me = ('Acerca de mi', validators=[DataRequired(), Length(min=0, max=200)])
    submit = SubmitField('Actualizar')