from . import admin_bp
from flask import render_template

from .auth import login_required


@admin_bp.get('/dashboard')
@login_required
def dashboard():
    module = 'dashboard'
    return render_template('admin/dashboard/index.html', module=module)
