from . import front_bp
from flask import render_template


@front_bp.get('/checkout')
def checkout():
    return render_template('front/checkout.html')
