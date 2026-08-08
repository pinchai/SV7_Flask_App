from . import front_bp
from flask import render_template


@front_bp.get('/account')
def account():
    return render_template('front/account.html')


@front_bp.get('/create-user')
def create_user():
    return render_template('front/create-user.html')
