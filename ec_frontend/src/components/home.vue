<script>
  export default {
    data () {
      return {
        menuList: [],
        iconObj: {
          '2 ': 'el-icon-user-solid',
          '3 ': 'el-icon-setting',
          '4 ': 'el-icon-s-shop',
          '5 ': 'el-icon-s-order',
          '6 ': 'el-icon-s-data'
        },
        active_path: '',
      }
    },
    created() {
      // 刚创建时就应该加载出菜单内容
      this.getMenuList()
      this.active_path = window.sessionStorage.getItem('active_path')
    },
    methods: {
      logout() {
        // 清空存储的token
        window.sessionStorage.clear()
        // 跳登录页
        this.$router.push('/login')
        this.$msg.error('You\'re logged out!')
      },
      test() {
        // 发一个带有token的请求
        const { data: res } = this.$axios.get('/user/test')
        console.log(res)
      },
      handleOpen(key, keyPath) {
        console.log(key, keyPath)
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath)
      },
      async getMenuList() {
        const { data: res } = await this.$axios.get('/menu')
        this.menuList = res.data
        console.log(this.menuList)
      },
      activate(acp) {
        // console.log(acp.index)
        window.sessionStorage.setItem('active_path', acp.index)  // 记住上次点的标签，等待读取，下次回溯的时候可以回来
        this.active_path = acp.index
      },
    }
  }
</script>

<template>
  <el-container class="home-container">
    <el-header>
      <div>
        <img src="../assets/imgs/Firefox.png" alt="Unable to load logo.">
        <span>Backstage management system</span>
      </div>
      <el-button type="primary" @click="logout">Logout</el-button>
    </el-header>
    <el-container>
      <el-aside width="200px">
        <el-menu :default-active="active_path"
                 class="el-menu-vertical-demo"
                 @open="handleOpen"
                 @close="handleClose"
                 background-color="#303133"
                 text-color="white"
                 active-text-color="#409EFF"
                 unique-opened
                 router>  <!-- router 给菜单按index编号添加路由 -->
          <el-submenu :index="item.id+''" v-for="item in menuList" :key="item.id">
            <template slot="title">
              <i :class="iconObj[item.id + ' ']"></i>
              <span>{{ item.name }}</span>
            </template>
            <el-menu-item :index="subItem.path" v-for="subItem in item.children" :key="subItem.id" @click="activate">
              <i :class="iconObj[item.id + ' ']"></i>
              <span>{{ subItem.name }}</span>
            </el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-main>
        <router-view></router-view> <!--welcome页面的占位符，welcome组件会显示在这-->
      </el-main>
    </el-container>
  </el-container>
</template>

<style lang="less" scoped>
.home-container {
  height: 100%;
}

.el-header {
  display: flex;
  background-color: lightblue;
  align-items: center;
  justify-content: space-between;
  color: darkblue;
  font-size: 30px;
  img {
    height: 50px;
    width: 50px;
    opacity: 90%;
    padding: 0 20px 0 0;
    //border: solid black 1px;
  }
  div {
    display: flex;
    align-items: center;
  }
}

.el-main {
  background-color: #d3d3d3;
}

.el-aside {
  background-color: #303133;
}
</style>
