from . import front_bp
from flask import render_template

@front_bp.get('/cart')
def cart():
    return render_template('front/cart.html')
