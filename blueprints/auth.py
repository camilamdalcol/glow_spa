from flask import Blueprint, render_template, redirect, url_for, flash
from forms.registration_form import RegistrationForm
from models.user import User  # Importe o modelo de usuário

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register.html', methods=['GET', 'POST'])
def register():
    from app import db  # Importe db dentro da rota
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            name = form.name.data
            email = form.email.data
            password = form.password.data
            confirm_password = form.confirm_password.data

            if password == confirm_password:
                new_user = User(username=name, email=email)
                new_user.set_password(password)
                db.session.add(new_user)
                db.session.commit()
                flash("Account created successfully!", "success")
                return redirect(url_for('auth.welcome'))
            else:
                flash("Passwords don't match", 'error')
        except Exception as e:
            flash("An error occurred while creating the account. Please try again later.", 'error')
            db.session.rollback()

    return render_template('register.html', form=form)

@auth_bp.route('/welcome.html')
def welcome():
    return render_template('welcome.html')
