from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, request
from flask_api.models import User
from flask_api.utils.message import to_dict_msg
import functools

'''
客户端自己存登录信息，首次登录时客户端拿到服务器给的加密token，
下次登录时再给服务器解密验证。
'''


def generate_auth_token(uid, expiration, **kwargs):
    # create encode object
    s = Serializer(current_app.config['SECRET_KEY_FOR_TESTING'], expires_in=expiration)

    data = {'id': uid}
    data.update(**kwargs)

    return s.dumps(data).decode()


# 验证token，返回false失败
def decode_auth_token(auth_token):
    s = Serializer(current_app.config['SECRET_KEY_FOR_TESTING'])
    try:
        data = s.loads(auth_token)
    except Exception:
        return False
    usr = User.query.filter_by(id=data['id']).first()
    return usr


# “需要登录”装饰器，被装饰的函数必须登录（带有有效token）才能用
def login_required(view_func):
    functools.wraps(view_func)

    def verify_token(*args, **kwargs):
        try:
            # 获取请求头中带来的token
            token = request.headers['token']
        except Exception:
            return to_dict_msg(1008)
        s = Serializer(current_app.config['SECRET_KEY_FOR_TESTING'])
        try:
            data = s.loads(token)
        except Exception:
            return to_dict_msg(1009)
        return view_func(*args, **kwargs)
    return verify_token
