"""
 Hello 

"""

from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, ValidationError

from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm


class ClientForm(BaseForm):
    # 账号
    account = StringField(validators=[DataRequired(message='账号不允许为空'),
                                      length(min=5, max=32)])
    # 密码
    secret = StringField()
    # 类型
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message='invalidate email')])
    secret = StringField(validators=[DataRequired(r'^[A-Za-z0-9_*&$#@]{6,22}$')])
    nickname = StringField(validators=[DataRequired(), length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()


class BookSearchForm(BaseForm):
    q = StringField(validators=[DataRequired()])


class TokenForm(BaseForm):
    token = StringField(validators=[DataRequired()])
