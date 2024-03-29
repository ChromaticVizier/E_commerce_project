from flask import request
from flask_api.user import user, user_api  # 这里导入的user包里的是蓝图
from flask_api import db
from flask_api import models
from flask_restful import Resource
import re


@user.route('/')
def index():
    return 'Hello World!'


class User(Resource):
    def get(self):
        pass

    def post(self):
        # 接收数据
        name = request.form.get('name')
        pwd = request.form.get('pwd')
        confirm_pwd = request.form.get('confirm_pwd')
        nick_name = request.form.get('nick_name')
        phone = request.form.get('phone')
        email = request.form.get('email')

        # 验证数据完整性
        if not all([name, pwd, confirm_pwd]):
            return {'status': 1000,
                    'msg': 'THE data is incomplete.'}

        # 确认完整，详细判断
        if len(name) < 1:
            return {'status': 1002,
                    'msg': 'The name is invalid.'}
        if len(pwd) < 1:
            return {'status': 1003,
                    'msg': 'The password is invalid.'}
        if pwd != confirm_pwd:
            return {'status': 1004,
                    'msg': 'The password is inconsistent.'}
        if not re.match(r'1[345678]\d{9}', phone):
            return {'status': 1005,
                    'msg': 'The phone number is invalid.'}
        if not re.match(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', email):
            return {'status': 1006,
                    'msg': 'The email address is invalid.'}

        # 完整且合法，判断是否有其他问题
        try:
            # 接收参数应该用方法，不能直接赋值到pwd上
            usr = models.User(name=name, password=pwd, nick_name=nick_name, phone=phone, email=email)
            db.session.add(usr)
            db.session.commit()
            return {'status': 200,
                'msg': 'Register successfully.'}

        except Exception:
            return {'status': 1007,
                    'msg': 'An error occurred.'}


user_api.add_resource(User, '/user/')


@user.route('/login/', methods=['POST'])
def login():
    name = request.form.get('name')
    pwd = request.form.get('pwd')

    # 这个函数要求传入的都是真值(都有值)，否则报错
    if not all([name, pwd]):
        return {'status': 1000,
                'msg': 'The data is incomplete.'}

    if len(name) > 1:
        usr = models.User.query.filter_by(name=name).first()
        if usr:
            if usr.check_password(pwd):
                return {'status': 200,
                        'msg': 'Login Successful.'}

    return {'status': 1001,
            'msg': 'The user name or password is incorrect.'}
