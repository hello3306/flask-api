"""
 Hello 

"""

from app.libs.redprint import Redprint

api = Redprint('user')


@api.route('/get')
def get_user():
    return 'user'


@api.route('/create')
def create_user():
    pass
