"""
 Hello 

"""

from app.libs.error import APIException


class ClientTypeError(APIException):
    # 400请求参数错误
    code = 400
    msg = 'client  is invalid'
    error_code = 1006
