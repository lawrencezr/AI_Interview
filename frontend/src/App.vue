<template>
  <div id="app">
    <el-container>
      <el-header>
        AI 面试官
      </el-header>
      <el-main>
        <router-view/>
      </el-main>
    </el-container>
  </div>
</template>

<style lang="scss">
  .el-header{
    height: 60px;
    line-height: 60px;
    font-size: 20px;
    background-color: #fff;
    border-bottom: 1px solid #DCDFE6;
  }
</style>
