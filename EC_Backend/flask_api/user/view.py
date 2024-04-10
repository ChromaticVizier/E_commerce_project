from flask import request
from flask_api.user import user, user_api  # 这里导入的user包里的是蓝图
from flask_api import db
from flask_api import models
from flask_restful import Resource
import re
from flask_api.utils.tokens import generate_auth_token, decode_auth_token, login_required
from flask_api.utils.message import to_dict_msg



@user.route('/')
def index():
    return 'Hello World!'


class User(Resource):
    def get(self):
        # 返回自己的用户数据
        try:
            id1 = int(request.args.get('id').strip())
            user1 = models.User.filter_by(id=id1).first()
            if user1:
                return to_dict_msg(200, user1.to_dict())
            else:
                return to_dict_msg(200, [], 'User not found')
        except Exception:
            return to_dict_msg()

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
            return to_dict_msg(1000)

        # 确认完整，详细判断
        if len(name) < 1:
            return to_dict_msg(1002)
        if len(pwd) < 1:
            return to_dict_msg(1003)
        if pwd != confirm_pwd:
            return to_dict_msg(1004)
        if not re.match(r'1[345678]\d{9}', phone):
            return to_dict_msg(1005)
        if not re.match(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', email):
            return to_dict_msg(1006)

        # 完整且合法，判断是否有其他问题
        try:
            # 接收参数应该用方法，不能直接赋值到pwd上
            usr = models.User(name=name, password=pwd, nick_name=nick_name, phone=phone, email=email)
            db.session.add(usr)
            db.session.commit()
            return to_dict_msg(200)

        except Exception:
            return to_dict_msg(1007)


@user.route('/login', methods=['POST'])
# @login_required
def login():
    name = request.form.get('name')
    pwd = request.form.get('pwd')

    # 这个函数要求传入的都是真值(都有值)，否则报错
    if not all([name, pwd]):
        return to_dict_msg(1000)

    if len(name) > 1:
        usr = models.User.query.filter_by(name=name).first()
        if usr:
            if usr.verify_password(pwd):
                # 验证成功，生成token
                token = generate_auth_token(usr.id, 10000000)
                # decode_auth_token(token)
                return to_dict_msg(200, data={'token': token})

    return to_dict_msg(1001)


@user.route('/test')
@login_required
def test_login_req():
    return to_dict_msg(200)


user_api.add_resource(User, '/user/')
