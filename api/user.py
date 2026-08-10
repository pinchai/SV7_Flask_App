from api import api_bp
from extensions import db
from sqlalchemy import text
import models


@api_bp.get('/user')
def user():
    module = 'user'
    sql = text("SELECT * FROM user")
    result = db.session.execute(sql)
    users = result.fetchall()
    rows = [dict(row._mapping) for row in users]
    return {
        'message': 'success',
        'data': rows
    }, 200