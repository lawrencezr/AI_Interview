<template>
  <div>
    <el-row align="middle">
      <el-col :span="8" :offset="8">
        <el-form ref="loginForm" :model="loginForm" :rules="loginRules" label-width="80px" label-position="left">
          <el-form-item label="用户名" prop="name">
            <el-input v-model="loginForm.name" placeholder="请输入用户名" prefix-icon=""></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input v-model="loginForm.password" placeholder="请输入密码" prefix-icon=""></el-input>
          </el-form-item>
          <el-form-item label="面试码" prop="interview_code">
            <el-input v-model="loginForm.interview_code" placeholder="请输入面试码" prefix-icon=""></el-input>
          </el-form-item>
          <el-form-item label="登陆身份" prop="identity">
            <el-radio-group v-model="loginForm.identity" prop="identity">
              <el-radio label="求职者"></el-radio>
              <el-radio label="面试官"></el-radio>
            </el-radio-group>
          </el-form-item>
        </el-form>
        <el-button class="login-button" @click="submitForm('loginForm')">登陆</el-button>
      </el-col>
    </el-row>

  </div>
</template>

<script>
    export default {
      name: "Login",
      data(){
          return{
            loginForm:{
              name:'',
              password:'',
              interview_code:'',
              identity:'',
            },
            loginRules:{
              name:[
                {required:true,message:'请输入用户名',trigger:'blur'}
              ],
              password:[
                {required:true,message:'请输入密码',trigger:'blur'}
              ],
              interview_code:[
                {required:true,message:'请输入面试码',trigger:'blur'}
              ],
              identity:[
                {required:true,message:'请选择身份',trigger:'change'}
              ],
            }
          }
      },
      methods:{
        submitForm(formName){
          this.$refs[formName].validate((valid)=>{
            if(valid){
              this.$message({
                message:'验证成功',
                type:'success'
              });
            }
            else {
              this.$message({
                message:'验证失败',
                type:'error'
              });
            }
          })
        }
      }

    }
</script>

<style scoped>
  .login-button{
    width: 100%;
  }
</style>
