<template>
    <el-container>
        <span class="logo">AI 面试官</span>
        <el-menu mode="horizontal" v-if="name">
            <el-submenu index="1">
                <template slot="title">{{name}}</template>
                <el-menu-item index="1-1" @click="logout">退出登陆</el-menu-item>
            </el-submenu>
        </el-menu>
    </el-container>
</template>

<script>
    import {getCookie,delCookie} from "../assets/Cookie";

    export default {
        name: "NavBar",
        data() {
            return {
                name:''
            }
        },
        methods: {
            logout(){
                delCookie('name')
                delCookie('identity')
                this.$router.push('/')
            }
        },
        mounted(){
            let uname = getCookie('name')
            this.name = uname
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
    margin-bottom: 40px;
  }
  .el-menu.el-menu--horizontal{
      border-bottom: 0px;
  }
  .logo{
      padding-left: 20px;
  }
</style>