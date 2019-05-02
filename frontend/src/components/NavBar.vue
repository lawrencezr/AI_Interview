<template>
    <el-container>
        <span class="logo">AI 面试官</span>
        <el-menu mode="horizontal">
            <el-submenu index="1">
                <template slot="title">用户名</template>
                <el-menu-item index="1-1">退出登陆</el-menu-item>
            </el-submenu>
        </el-menu>
    </el-container>
</template>

<script>
    export default {
        name: "NavBar",
        data() {
            return {

            }
        }
    }
</script>

<style scoped>
  .el-container{
    height: 61px;
    line-height: 61px;
    font-size: 20px;
    background-color: #fff;
    border-bottom: 1px solid #DCDFE6;
    justify-content: space-between;
    margin-left: 20px;
    margin-right: 20px;
  }
  .el-menu.el-menu--horizontal{
      border-bottom: 0px;
  }
  .logo{
      margin-left: 20px;
  }
  /*.headerWrapper {*/
      /*height: 80px;*/
  /*}*/
/*.header {*/
    /*height: 80px;*/
    /*top: 0;*/
    /*left: 0;*/
    /*width: 100%;*/
    /*line-height: 80px;*/
    /*z-index: 100;*/
    /*position: relative;*/
        /*.container {*/
      /*height: 100%;*/
      /*box-sizing: border-box;*/
      /*border-bottom: 1px solid #DCDFE6;*/
    /*}*/
/*}*/
    /*.nav {*/
      /*float: right;*/
      /*height: 100%;*/
      /*line-height: 80px;*/
      /*background: transparent;*/
      /*padding: 0;*/
      /*margin: 0;*/
    /*}*/
    /*.nav-item {*/
        /*margin: 0;*/
      /*float: left;*/
      /*list-style: none;*/
      /*position: relative;*/
      /*cursor: pointer;*/
    /*}*/
</style>