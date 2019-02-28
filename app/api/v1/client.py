"""
 Hello 

"""
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ClientTypeError
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint('client')


# 客户端注册
@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm().validate_form_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email,
        # ClientTypeEnum.USER_MINA:
    }
    promise[form.type.data]()
    return 'success'


# 邮件注册
def __register_user_by_email():
    form = UserEmailForm().validate_form_api()
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
