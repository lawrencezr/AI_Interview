<template>
  <div id="app">
      <router-view/>
  </div>
</template>
<script>
  import {getCookie} from "./assets/Cookie";

  export default {
      name:'app',
      created(){
          if(!getCookie('name')){
              this.$router.push('/login')
          }
      }
  }
</script>
<style lang="scss">
  .el-header{
    height: 60px;
    line-height: 60px;
    font-size: 20px;
    background-color: #fff;
    border-bottom: 1px solid #DCDFE6;
  }
</style>
