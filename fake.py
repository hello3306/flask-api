"""
Create by 2019/3/7 21:00
"""
from app import create_app
from app.models.base import db
from app.models.user import User

app = create_app()

with app.app_context():
    with db.auto_commit():
        user = User()
        user.nickname = 'Super'
        user.password = '123456'
        user.email = '1359441823@qq.com'
        user.auth = 2
        db.session.add(user)
