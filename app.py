from flask import Flask, render_template, redirect, url_for, request
import random
from product import products as pro, get_product_by_category

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import text

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile = db.Column(db.String(80), nullable=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(120), nullable=False, default='admin')


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
    sql = text("SELECT * FROM user")
    result = db.session.execute(sql)
    users = result.fetchall()
    rows = [dict(row._mapping) for row in users]
    return render_template(
        'admin/user/index.html',
        module=module,
        rows=rows,
    )


@app.get('/admin/user/add')
def add_user():
    module = 'user'
    return render_template('admin/user/add.html', module=module)


@app.get('/admin/user/edit/<int:user_id>')
def edit_user(user_id):
    module = 'user'
    return render_template('admin/user/edit.html', module=module, user_id=user_id)


@app.get('/admin/user/confirm-delete/<int:user_id>')
def confirm_delete(user_id):
    module = 'user'
    sql = text("SELECT * FROM user where id = :user_id")
    result = db.session.execute(sql, {"user_id": user_id})
    user = dict(result.fetchone()._mapping)
    return render_template('admin/user/confirm_delete.html', module=module, user=user)


@app.post('/admin/user/delete')
def delete_user():
    module = 'user'
    form = request.form
    user_id = int(form.get('user_id'))
    sql = text("DELETE FROM user WHERE id = :user_id")
    db.session.execute(sql, {"user_id": user_id})
    db.session.commit()
    return redirect(url_for('user'))


if __name__ == '__main__':
    app.run()
