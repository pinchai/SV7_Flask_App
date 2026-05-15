from flask import Flask, render_template
import random

app = Flask(__name__)


@app.get('/')
def home():
    return render_template('front/index.html')


@app.get('/products')
def products():
    return render_template('front/products.html')


@app.get('/product')
def product():
    return render_template('front/product.html')


@app.get('/cart')
def cart():
    return render_template('front/cart.html')


@app.get('/account')
def account():
    return render_template('front/account.html')


@app.get('/forgot-password')
def forgot_password():
    return render_template('front/forgot-password.html')


@app.get('/login')
def login():
    return render_template('front/login.html')


@app.get('/create-user')
def create_user():
    return render_template('front/create-user.html')


@app.get('/checkout')
def checkout():
    return render_template('front/checkout.html')


@app.get('/test_template')
def test_template():
    from product import products
    for item in products:
        item['qty'] = random.randint(1, 100)
        item['discount_pct'] = random.randint(0, 100)
        item['name'] = item['title'][:20]

    # assert False, products[0]

    return render_template(
        'test_template.html',
        products=products,
    )


if __name__ == '__main__':
    app.run()
