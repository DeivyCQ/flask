from app import app
from flask import render_template, request, flash, redirect, url_for
from app.forms.login import LoginForm
from flask_login import current_user, login_user
from app.models.user import User
from werkzeug.urls import url_parse

@app.route("/")
@app.route("/inicio")
def index():
    return render_template('index.html', title='Inicio')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(f'No se encuentra el usuario')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('views/login.html', title='Login', form=form)