from . import admin_bp
from flask import render_template

from flask import request, redirect, url_for
from werkzeug.security import generate_password_hash

from extensions import db
from sqlalchemy import text
import models


@admin_bp.get('/user')
def user():
    module = 'user'
    sql = text("SELECT * FROM user")
    result = db.session.execute(sql)
    users = result.fetchall()
    rows = [dict(row._mapping) for row in users]
    return render_template(
        'admin/user/index.html',
        module=module,
        rows=rows,
    )


@admin_bp.get('/user/add')
def add_user():
    module = 'user'
    return render_template('admin/user/add.html', module=module)


@admin_bp.post('/user/add')
def add():
    form = request.form
    user = models.User(
        username=form.get('username'),
        email=form.get('email'),
        password=generate_password_hash(form.get('password')),
        role=form.get('role'),
    )
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('admin_bp.user'))


@admin_bp.get('/user/edit/<int:user_id>')
def edit_user(user_id):
    module = 'user'
    sql = text("SELECT * FROM user where id = :user_id")
    result = db.session.execute(sql, {"user_id": user_id})
    user = dict(result.fetchone()._mapping)

    return render_template(
        'admin/user/edit.html',
        module=module,
        user=user
    )


@admin_bp.post('/user/edit')
def edit():
    form = request.form
    user = models.User.query.get(form.get('user_id'))

    user.username = form.get('username')
    user.email = form.get('email')
    user.role = form.get('role')
    if form.get('password'):
        user.password = generate_password_hash(form.get('password'))
    db.session.commit()

    return redirect(url_for('admin_bp.user'))


@admin_bp.get('/user/confirm-delete/<int:user_id>')
def confirm_delete(user_id):
    module = 'user'
    sql = text("SELECT * FROM user where id = :user_id")
    result = db.session.execute(sql, {"user_id": user_id})
    user = dict(result.fetchone()._mapping)
    return render_template('admin/user/confirm_delete.html', module=module, user=user)


@admin_bp.post('/user/delete')
def delete_user():
    module = 'user'
    form = request.form
    user_id = int(form.get('user_id'))
    sql = text("DELETE FROM user WHERE id = :user_id")
    db.session.execute(sql, {"user_id": user_id})
    db.session.commit()
    return redirect(url_for('admin_bp.user'))
