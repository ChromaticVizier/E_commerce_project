<script>
  export default {
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
        const {data: res} = this.$axios.get('/user/test')
        console.log(res)
      }
    }
  }
</script>

<template>
  <el-container class="home-container">
    <el-header>
      <div>
        <img src="../assets/imgs/Firefox.png">
        <span>Backstage management system</span>
      </div>
      <el-button @click="test">Test</el-button>
      <el-button type="primary" @click="logout">Logout</el-button>
    </el-header>
    <el-container>
      <el-aside width="200px">Aside</el-aside>
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
