from flask_api import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class BaseModel:
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


# 继承数据库对象db的模型，映射时可以直接找到db对应的数据库
class User(db.Model, BaseModel):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    pwd = db.Column(db.String(128))
    nick_name = db.Column(db.String(32))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(32))

    # 关于密码存储：
    # 1、用户注册时输入初始密码
    # 2、经过哈希散列存到数据库
    # 3、用户登录时输入密码
    # 4、散列后和数据库里的比对看一不一样

    # 外边想拿password时通过这个函数拿，直接返回真实密码
    # 加property装饰器后，调用方法时不再需要小括号
    @property
    def password(self):
        return self.pwd
    
    # password方法此时已经成为私有属性，必须通过setter方法赋值
    # 用于生成散列
    @password.setter
    def password(self, t_pwd):
        self.pwd = generate_password_hash(t_pwd)

    def verify_password(self, t_pwd):
        return check_password_hash(self.pwd, t_pwd)
