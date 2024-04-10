from flask import request
from flask_api.user import user, user_api  # 这里导入的user包里的是蓝图
from flask_api import db
from flask_api import models
from flask_restful import Resource, reqparse
import re
from flask_api.utils.tokens import generate_auth_token, login_required
from flask_api.utils.message import to_dict_msg


@user.route('/')
def index():
    return 'Hello World!'


'''==============================用户操作=============================='''


class User(Resource):
    def get(self):
        # 返回自己的用户数据
        try:
            id1 = int(request.args.get('id').strip())
            user1 = models.User.query.filter_by(id=id1).first()
            if user1:
                return to_dict_msg(200, user1.to_dict())
            else:
                return to_dict_msg(200, [], 'User not found')
        except Exception:
            return to_dict_msg(1000)

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

    # 要修改信息用put请求
    def put(self):
        try:
            id1 = int(request.form.get('id').strip())
            email = request.form.get('email').strip() if request.form.get('email') else None
            phone = request.form.get('phone').strip() if request.form.get('phone') else None
            user1 = models.User.query.get(id1)
            if user1:
                # 传了再改
                if email:
                    user1.email = email
                if phone:
                    user1.phone = phone
                # 改完数据别忘提交
                db.session.commit()
                return to_dict_msg(200)
            else:
                return to_dict_msg(1010, msg='User does not exist!')
        except Exception as e:
            print(e)
            return to_dict_msg(1000)

    # 用于删除用户
    def delete(self):
        try:
            id1 = int(request.form.get('id').strip())
            user1 = models.User.query.get(id1)
            if user1:
                db.session.delete(user1)
                db.session.commit()
                return to_dict_msg(200, msg='User deleted!')
            else:
                return to_dict_msg(1011, msg='User does not exist!')
        except Exception as e:
            print(e)
            return to_dict_msg(1000)


'''==============================用户操作=============================='''


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


class UserList(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        # 用来代替request.args.get()获取参数
        # 类似wtform验证，自动类型转换
        #                                 这个参数必须有，指定把参数绑在哪
        parser.add_argument('name', location='args', type=str)
        parser.add_argument('pagenum', location='args', type=int)
        parser.add_argument('pagesize', location='args', type=int)
        try:
            args = parser.parse_args()
            name = args.get('name')
            pagenum = args.get('pagenum') if args.get('pagenum') else 1  # 如果没传，设默认值
            pagesize = args.get('pagesize') if args.get('pagesize') else 2
            if name:
                # 模糊查询姓名
                user1 = models.User.query.filter(
                    models.User.name.like(f'%{name}%')
                ).paginate(page=pagenum, per_page=pagesize)  # 分页
            else:
                user1 = models.User.query.paginate(page=pagenum, per_page=pagesize)
            data = {
                'pagenum': pagenum,
                'totalpages': user1.total,
                'users': [u.to_dict() for u in user1.items]
            }
            return to_dict_msg(200, data=data)

        except Exception as e:
            print(e)
            return to_dict_msg(1000)


@user.route('/test')
@login_required
def test_login_req():
    return to_dict_msg(200)


user_api.add_resource(User, '/user/')
user_api.add_resource(UserList, '/userlist/')
