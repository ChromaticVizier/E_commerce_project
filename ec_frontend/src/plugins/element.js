import Vue from 'vue'
import { Button } from 'element-ui'
import { Form, FormItem, Input, Message } from 'element-ui'

Vue.use(Button)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)

// 弹窗当作属性用，需要挂载
Vue.prototype.$msg = Message
