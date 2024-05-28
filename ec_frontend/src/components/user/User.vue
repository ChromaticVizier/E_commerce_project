<script>
  export default {
    data() {
      return {
        userList: [],
        queryInfo: {
          pagenum: 1,
          pagesize: 10,
        },
        totalusernum: 0,
    }
  },
  methods: {
    async getUserList() {
      const { data:res } = await this.$axios.get('user/userlist', { params: this.queryInfo })
      if (res.status !== 200) return this.$msg.error(res.msg)
      this.totalusernum = res.data.totalpages
      this.userList = res.data.users
      console.log(this.userList)
    },
    handleSizeChange(val) {
      this.queryInfo.pagesize = val
      this.getUserList()
      console.log(`${val} items per page`);
    },
    handleCurrentChange(val) {
      this.queryInfo.pagenum = val
      this.getUserList()
      console.log(`current page: ${val}`);
    }
  },
  created() {
    this.getUserList()
  }
}

</script>

<template>
  <div>
    <!-- 面包屑 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">Homepage</el-breadcrumb-item>
      <el-breadcrumb-item>User management</el-breadcrumb-item>
      <el-breadcrumb-item>User list</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card>
      <el-row>
        <el-col :span="8">
          <div>
            <el-input placeholder="Please input" class="input-with-select">
              <el-button icon="el-icon-search"></el-button>
            </el-input>
          </div>
        </el-col>
        <el-col :span="2">
          <el-button type="primary" icon="el-icon-plus">New user</el-button>
        </el-col>
      </el-row>
      <el-row>
        <el-col>
          <el-table :data="userList" style="width: 100%">
            <el-table-column prop="id"          label="ID"></el-table-column>
            <el-table-column prop="name"        label="Name"></el-table-column>
            <el-table-column prop="nick name"   label="Nickname"></el-table-column>
            <el-table-column prop="email"       label="Email"></el-table-column>
            <el-table-column prop="phone"       label="Phone"></el-table-column>
            <el-table-column                    label="Actions">
              <template slot-scope="scope">
                <el-button
                  size="mini"
                  @click="handleEdit(scope.$index, scope.row)">Edit</el-button>
                <el-button
                  size="mini"
                  type="danger"
                  @click="handleDelete(scope.$index, scope.row)">Delete</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-col>
      </el-row>
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page.sync="queryInfo.pnum"
        :page-sizes="[10, 20, 30, 50, 100, 150, 200]"
        :page-size="queryInfo.psize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="totalusernum">
      </el-pagination>
    </el-card>
  </div>
</template>

<style scoped lang="less">

</style>
