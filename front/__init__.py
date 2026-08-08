from flask import Blueprint

front_bp = Blueprint('front_bp', __name__,
                     template_folder='templates')
from . import home
from . import product
from . import cart
from . import account
from . import checkout
from . import user_auth
