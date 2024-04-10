import Vue from 'vue'
import VueRouter from 'vue-router'
import login from '../components/login.vue'
import home from '../components/home.vue'
import welcome from '../components/welcome.vue'

Vue.use(VueRouter)

// 增加路由地址时往这里边写
const routes = [
  {
    path: '/login',
    component: login
  },
  {
    path: '/home',
    component: home,
    redirect: '/welcome',
    children: [
      {
        path: '/welcome',
        component: welcome
      }
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router

// 自动跳转到登录界面
//                       到哪去      从哪来        下一步（本来要执行的操作）
router.beforeEach((to, form, next) => {
  // 如果本来就要登录，直接放过去
  if(to.path === '/login') return next()
  // 如果访问别的页，拿token看看是否有效
  const tokenStr = window.sessionStorage.getItem('token')
  // 如果token无效，跳到登录页
  if(!tokenStr) {
    return next('/login')
  }
  next()
})
