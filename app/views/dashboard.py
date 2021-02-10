from flask import Blueprint, redirect, render_template, url_for, flash
from flask_login import login_required
from app import forms, models

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@bp.route("/", methods=["GET"])
@login_required
def index():
	return render_template("dashboard.html")