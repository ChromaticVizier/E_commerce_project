<script>
export default {
  data() {
    return {
      // 登录表单，这里边的数据绑定输入框的v-model属性
      userForm: {
        name: '',
        pwd: ''
      },
      // 表单验证，这里边的数据绑定prop属性，设置用谁来验证
      userRules: {
        // 列表里写具体验证规则
        name: [
          { required: true, message: 'Username cannot be empty.', trigger: 'blur' },
          { min: 1, max: 128, message: 'Username should be between 1 and 128 characters long.', trigger: 'blur' }
        ],
        pwd: [
          { required: true, message: 'Password cannot be empty.' },
          { min: 1, max: 20, message: 'Password should be between 1 and 20 characters long.', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    resetForm() {
      // this指向表单对象，这一行是调用表单自己的reset方法
      // ref用来绑定表单元素，写在form最外层
      // 外边可以用ref的值（这里是userRef）来绑定表单
      // restFields会重置到默认值，不设就是清空
      this.$refs.userRef.resetFields()
    },
    login() {
      // 登陆前应该再验证一次数据有效性
      // 这个函数，只有整个表单都有效valid才会是true
      this.$refs.userRef.validate(async valid => {
        // console.log(valid)
        if(!valid) return
        // 有效，登录
        // 这里发的是异步请求，加一个await来等待返回结果（注意要在函数前边加上async）
        const { data: res } = await this.$axios.post('/user/login', this.$qs.stringify(this.userForm))
        // 把请求的响应赋给res                                     把表单转成字符串方便调试
        if (res.status === 200) {
          // 登录成功后拿到token，存到sessionStorage里
          window.sessionStorage.setItem('token', res.data.token)
          // 登录成功弹窗
          this.$msg.success(res.msg)
          // 跳转
          await this.$router.push('/home')
        }
        else {
          // 不成功，直接弹错误信息
          this.$msg.error(res.msg)
        }
      })
    }
  }
}
</script>

<template>
  <div class="login_container">
    <div class="login_box">
      <div class="login_logo">
        <img src="../assets/imgs/Firefox.png">
      </div>
      <el-form :rules="userRules" :model="userForm" ref="userRef" label-width="0px" class="form_style">
        <el-form-item prop="name">
          <el-input v-model="userForm.name" placeholder="Username" prefix-icon="el-icon-user-solid"></el-input>
        </el-form-item>
        <el-form-item prop="pwd">
          <el-input type="password" v-model="userForm.pwd" placeholder="Password" prefix-icon="el-icon-s-check"></el-input>
        </el-form-item>
        <el-form-item class="button_style">
          <el-button @click="login" type="primary">Login</el-button>
          <el-button @click="resetForm">Reset</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<style lang="less" scoped>
.login_container {
  background-color: cornflowerblue;
  height: 100%;
}

.login_box {
  width: 450px;
  height: 300px;
  border-radius: 10px;
  background-color: azure;
  opacity: 90%;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.login_logo {
  height: 100px;
  width: 100px;
  position: absolute;
  left: 50%;
  transform: translate(-50%, -50%);
  img {
    opacity: 70%;
    width: 100%;
    height: 100%;
  }
}

.form_style {
  position: absolute;
  bottom: 0;
  width: 100%;
  padding: 5% 5%;
  // 上下，左右
  box-sizing: border-box;
  // 防止宽度为100%的东西设置偏移后超出盒模型
}

.button_style {
  display: flex;
  justify-content: flex-end;
}
</style>
