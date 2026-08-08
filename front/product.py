from . import front_bp
from flask import render_template

from product import products as pro, get_product_by_category


@front_bp.get('/products')
def products():
    return render_template('front/products.html', products=pro)


@front_bp.get('/product/<product_name>')
def product(product_name):
    from product import get_product_by_title
    product = get_product_by_title(product_name)
    related_product = get_product_by_category(product['category'])
    return render_template(
        'front/product.html',
        product=product,
        related_product=related_product,
    )

