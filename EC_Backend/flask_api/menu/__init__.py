from flask import Blueprint
from flask_restful import Api

menu = Blueprint('menu', __name__)
# Api对象要在蓝图里拿
menu_api = Api(menu)

from flask_api.menu import view
