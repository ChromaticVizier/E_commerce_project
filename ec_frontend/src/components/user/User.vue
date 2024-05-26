<script>
  export default {
    data() {
      return {
        tableData: [],
    }
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
          <el-table :data="tableData" style="width: 100%">
            <el-table-column prop="id" label="ID"></el-table-column>
            <el-table-column prop="name" label="Name"></el-table-column>
            <el-table-column prop="nickname" label="Nickname"></el-table-column>
            <el-table-column prop="email" label="Email"></el-table-column>
            <el-table-column prop="phone" label="Phone"></el-table-column>
            <el-table-column prop="actions" label="Actions"></el-table-column>
          </el-table>
        </el-col>
      </el-row>
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page.sync="currentPage4"
        :page-sizes="[100, 200, 300, 400]"
        :page-size="100"
        layout="total, sizes, prev, pager, next, jumper"
        :total="400">
      </el-pagination>
    </el-card>
  </div>
</template>

<style scoped lang="less">

</style>
