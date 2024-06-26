import Vue from 'vue'
import { Button } from 'element-ui'
import { Form, FormItem, Input, Message } from 'element-ui'
import { Container, Header, Aside, Main } from 'element-ui'
import { Menu, Submenu, MenuItemGroup, MenuItem } from 'element-ui'
import { Breadcrumb, BreadcrumbItem } from 'element-ui'
import { Card } from "element-ui"
import { Col, Row } from "element-ui"
import { Table, TableColumn } from "element-ui"
import { Pagination } from "element-ui"

Vue.use(Button)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)
Vue.use(Container)
Vue.use(Header)
Vue.use(Aside)
Vue.use(Main)
Vue.use(Menu)
Vue.use(Submenu)
Vue.use(MenuItemGroup)
Vue.use(MenuItem)
Vue.use(Breadcrumb)
Vue.use(BreadcrumbItem)
Vue.use(Card)
Vue.use(Col)
Vue.use(Row)
Vue.use(Table)
Vue.use(TableColumn)
Vue.use(Pagination)

// 弹窗当作属性用，需要挂载
Vue.prototype.$msg = Message
