from flask_api import db
from flask_api import models
from faker import Faker
from manager import app


# manager = user_api.manager

f = Faker(locale='en_US')
f1 = Faker(locale='zh_CN')

def insert_user():
    # name = request.form.get('name')
    # pwd = request.form.get('pwd')
    # confirm_pwd = request.form.get('confirm_pwd')
    # nick_name = request.form.get('nick_name')
    # phone = request.form.get('phone')
    # email = request.form.get('email')
    with app.app_context():
        for i in range(50):
            name = f.name()
            pwd = f.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
            nick_name = f1.name()
            phone = f1.phone_number()
            email = f.email()
            usr = models.User(name=name, password=pwd, nick_name=nick_name, phone=phone, email=email)
            db.session.add(usr)
            db.session.commit()

if __name__ == '__main__':
    insert_user()