from Clean import app, db
from flask import render_template, flash, redirect, url_for
from Clean.forms import RegisterForm, LoginForm
from Clean.models import User, Post
from flask_login import login_user, current_user, logout_user

@app.route('/')
def index():
    return render_template('index.html', title= 'Homes')

@app.route('/about')
def about():
    return render_template('about.html', title= 'about')

@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))   
    form=RegisterForm()
    if form.validate_on_submit():
        user= User(name=form.name.data, email = form.email.data, password= form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'{form.name.data} account created', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title= 'register',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash(f' Başarısız ULAN ','danger')
    return render_template('login.html', title= 'login',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
