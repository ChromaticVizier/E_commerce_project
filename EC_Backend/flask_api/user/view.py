from flask_api.user import user  # 这里导入的user包里的是蓝图
from flask_api import models


@user.route('/')
def index():
    return 'Hello World!'
