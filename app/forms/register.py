from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError
from app.models.user import User

class RegisterForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    email = ('Correo', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    password2 = PasswordField('Repetir Contraseña', validators=[DataRequired(), EqualTo()])
    submit = SubmitField('Registrar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            return ValidationError(f'El usuario {username.data} ya existe, intente con otro!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            return ValidationError(f'El correo {email.data} ya existe, intente con otro !')