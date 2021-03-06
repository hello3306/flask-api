"""
 Hello 

"""

from app.libs.error import APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    code = 202
    error_code = 1


class ServerError(APIException):
    code = 500
    msg = 'sorry,server exception'
    error_code = 999


class ClientTypeError(APIException):
    # 400请求参数错误
    code = 400
    msg = 'client  is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid paramter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'the resource are not_fund'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed'
    error_code = 1005


class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = "Forbidden,not in scope"


class DuplicateGift(APIException):
    code = 400
    error_code = 2001
    msg = 'the current book has already in gift'
