from flask_api.menu import menu, menu_api
from flask_api import models, db
from flask import request
from flask_restful import Resource
from flask_api.utils.message import to_dict_msg


class Menu(Resource):
    def get(self):
        type_ = request.args.get('type')
        # 在请求里传一个参数，根据type_参数选择返回list还是tree
        menu_list = []
        if type_ == 'list':
            # 在这填充menu数据
            mu = models.Menu.query.filter(models.Menu.level != 0).all()
            for m in mu:
                menu_list.append(m.to_dict())

        else:
            mu = models.Menu.query.filter(models.Menu.level == 1).all()
            for m in mu:
                # 一级菜单转成json
                first_menu = m.to_dict()
                # 创建保存二级菜单的容器
                first_menu['children'] = []
                for child in m.children:
                    # 把二级菜单转成json
                    second_dict = child.to_dict()
                    second_dict['children'] = child.get_child_list()
                    # 绑定二级和一级
                    first_menu['children'].append(second_dict)
                menu_list.append(first_menu)
        return to_dict_msg(200, data=menu_list)


menu_api.add_resource(Menu, '/menu/')
