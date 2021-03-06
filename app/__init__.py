"""
 Hello 

"""
from app.app import Flask


def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)

    # 加载配置文件
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    # 蓝图注册
    register_blueprints(app)

    # 数据库模型的注册
    register_plugin(app)

    return app
