<script>
  export default {
    data () {
      return {
        menuList: []
      }
    },
    created() {
      // 刚创建时就应该加载出菜单内容
      this.getMenuList()
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
        <el-menu default-active="2"
                 class="el-menu-vertical-demo"
                 @open="handleOpen"
                 @close="handleClose"
                 background-color="#545c64"
                 text-color="#fff"
                 active-text-color="#ffd04b">
          <el-submenu index="1" v-for="item in menuList" :key="item.id">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>{{ item.name }}</span>
            </template>
            <el-menu-item v-for="subitem in item.children" :key="subitem.id">
              <i class="el-icon-bell"></i>
              <span>{{ subitem.name }}</span>
            </el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-main>Main</el-main>
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
  background-color: #8888;
}

.el-aside {
  background-color: #999;
}
</style>
