from flask import Blueprint
from flask_restful import Api

user = Blueprint('user', __name__, url_prefix='/user')
# Api对象要在蓝图里拿
user_api = Api(user)

from flask_api.user import view
