import Vue from 'vue'
import { Button } from 'element-ui'
import { Form, FormItem, Input, Message } from 'element-ui'
import { Container, Header, Aside, Main } from 'element-ui'
import {Menu, Submenu, MenuItemGroup, MenuItem} from "element-ui";

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

// 弹窗当作属性用，需要挂载
Vue.prototype.$msg = Message
