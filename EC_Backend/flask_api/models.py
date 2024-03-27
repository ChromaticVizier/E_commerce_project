from flask_api import db
from werkzeug.security import generate_password_hash


# 继承数据库对象db的模型，映射时可以直接找到db对应的数据库
class User(db.Model):
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

    # 想拿password时通过这个函数拿
    @property
    def password(self):
        return self.pwd

    # 用于生成散列
    @password.setter
    def password(self, t_pwd):
        self.pwd = generate_password_hash(t_pwd)

    def verify_password(self, t_pwd):
