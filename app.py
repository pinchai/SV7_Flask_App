from flask import Flask, render_template
import random
from product import products as pro, get_product_by_category

app = Flask(__name__)


@app.get('/')
def home():
    return render_template('front/index.html', products=pro)


@app.get('/products')
def products():
    return render_template('front/products.html', products=pro)


@app.get('/product/<product_name>')
def product(product_name):
    from product import get_product_by_title
    product = get_product_by_title(product_name)
    related_product = get_product_by_category(product['category'])
    return render_template(
        'front/product.html',
        product=product,
        related_product=related_product,
    )


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


@app.get('/admin/dashboard')
def dashboard():
    module = 'dashboard'
    return render_template('admin/dashboard/index.html', module=module)


@app.get('/admin/user')
def user():
    module = 'user'
    users = [
        {
            'id': 1,
            'username': 'admin',
            'email': 'admin@localhost.com',
            'role': 'admin',
        }
    ]
    return render_template(
        'admin/user/index.html',
        module=module,
        users=users,
    )


@app.get('/admin/user/add')
def add_user():
    module = 'user'
    return render_template('admin/user/add.html', module=module)


if __name__ == '__main__':
    app.run()
