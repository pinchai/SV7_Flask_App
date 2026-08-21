from . import admin_bp
from flask import render_template

from flask import request, redirect, url_for, session
from werkzeug.security import check_password_hash
from functools import wraps

from extensions import db
from sqlalchemy import text
import models


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("is_login"):
            return redirect(url_for("admin_bp.admin_login", next=request.path))
        return view(*args, **kwargs)

    return wrapped


@admin_bp.get('/login')
def admin_login():
    session.clear()
    return render_template('admin/login.html', )


@admin_bp.post('/login')
def admin_do_login():
    form = request.form
    username = form.get('username').strip()
    password = form.get('password')
    user = models.User.query.filter_by(username=username).first()
    if user is None:
        return redirect(url_for('admin_bp.admin_login'))

    if check_password_hash(user.password, password):
        session['is_login'] = True
        session['user_id'] = user.id
        session['profile'] = user.profile
        session['username'] = user.username
        session['email'] = user.email
        session['role'] = user.role
        return redirect(url_for('admin_bp.dashboard'))
    else:
        session.clear()
        return redirect(url_for('admin_bp.admin_login'))


@admin_bp.get('/logout')
def admin_logout():
    session.clear()
    return redirect(url_for('admin_bp.admin_login'))
