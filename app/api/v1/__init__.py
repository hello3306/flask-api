"""
 Hello 

"""
from flask import Blueprint

from app.api.v1 import user, book, client, token


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    # 红图的注册
    Redprint = [user, book, client, token]
    for red in Redprint:
        red.api.register(bp_v1)
    # user.api.register(bp_v1)
    # book.api.register(bp_v1)
    # client.api.register(bp_v1)

    return bp_v1
