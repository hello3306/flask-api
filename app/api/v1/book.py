"""
 Hello 

"""

from app.libs.redprint import Redprint

api = Redprint('book')


@api.route('', methods=['GET'])
def get_book():
    return 'get book'
