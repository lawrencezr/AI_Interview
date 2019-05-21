<template>
    <el-container>
        <span class="logo">AI 面试官</span>
        <el-menu mode="horizontal" v-if="name">
            <el-menu-item v-if="identity == 'admin'" index="/train">
                样例打分
            </el-menu-item>
            <el-submenu v-if="identity == 'admin'"  index="2">
                <template slot="title">面试结果</template>
                <el-menu-item index="/performance">
                    查看结果
                </el-menu-item>
                <el-menu-item index="2-2">
                    导出名单
                </el-menu-item>
            </el-submenu>
            <el-submenu index="3">
                <template slot="title">{{name}}</template>
                <el-menu-item index="3-1" @click="logout">退出登陆</el-menu-item>
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
                name:'',
                identity:'',
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
            let uidentity = getCookie('identity')
            this.name = uname
            this.identity = uidentity
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