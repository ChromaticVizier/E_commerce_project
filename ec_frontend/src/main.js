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

axios.defaults.baseURL = 'http://localhost:5000'
// 让axios默认把请求发到这个地址

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
