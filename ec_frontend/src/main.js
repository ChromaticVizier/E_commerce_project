import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import './assets/global.css'
import axios from 'axios'
import qs from 'qs'

Vue.config.productionTip = false
Vue.prototype.$axios = axios
//            随意起名
Vue.prototype.$qs = qs

// axios.defaults.baseURL = 'http://localhost:5000'
// 让axios默认把请求发到这个地址

// 请求拦截器：访问后端时拿出token并放在请求里
// use要求传一个操作函数作为参数
axios.interceptors.request.use(
  // config就是请求体
  config => {
    const tokenStr = window.sessionStorage.getItem('token')
    if(tokenStr) {
      config.headers.token = tokenStr
      // 把token放进请求头
    }
    return config
  })

// 响应拦截器（如果token无效就跳登录界面）
axios.interceptors.response.use(
  response => {
    if(response.data.status === 1008 || response.data.status === 1009) {
      // 如果没token或者已过期：删掉本地的token
      window.sessionStorage.removeItem('token')
      // 跳登录界面
      router.replace(
        {
          path: '/login'
        })
    }
    return response
  })

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
