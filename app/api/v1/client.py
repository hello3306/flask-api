"""
 Hello 

"""
from app.libs.redprint import Redprint

api = Redprint('client')


# 客户端注册
@api.route('/register')
def create_client():

    pass
