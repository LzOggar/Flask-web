from flask import Blueprint, redirect, render_template, url_for, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from bleach import clean
from app import forms, models, db, login_manager

bp = Blueprint("auth", __name__, url_prefix="/auth")

@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(user_id)

@bp.route("/login", methods=["GET","POST"])
def login():
	if current_user.is_authenticated:
		return redirect(url_for("dashboard.index"))

	form = forms.Login()	

	if form.validate_on_submit():
		username = form.username.data
		password = form.password.data
		error = None

		user = models.User.query.filter_by(username=username).first()
		
		if user is None or not user.check_password(password):
			error = "Invalid username or password."

		if error is None:
			login_user(user)
			return redirect(url_for("dashboard.index"))
		
		flash(error, "danger")

	return render_template("auth/login.html", form=form)

@bp.route("/logout", methods=["GET"])
@login_required
def logout():
	logout_user()
	return redirect(url_for("auth.login"))

@bp.route("/register", methods=["GET","POST"])
def register():
	if current_user.is_authenticated:
		return redirect(url_for("auth.login"))

	form = forms.Register()

	if form.validate_on_submit():
		error = None
		username = clean(form.username.data, tags=[], strip=True)
		password = clean(form.password.data, tags=[], strip=True)
		confirm_password = clean(form.confirm_password.data, tags=[], strip=True)
		email = clean(form.email.data, tags=[], strip=True)

		user = models.User.query.filter_by(username=username).first()
		if user is None:
			if password == confirm_password:
				user = models.User(username=username, email=email)
				user.set_password(password)

				db.session.add(user)
				db.session.commit()

				login_user(user)
				return redirect(url_for("dashboard.index"))
			else:
				flash("Password are not equals.", "danger")

	return render_template("auth/register.html", form=form)