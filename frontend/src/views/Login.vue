<template>
  <div>
    <el-row align="middle">
      <el-col :span="8" :offset="8">
        <el-form ref="loginForm" :model="loginForm" :rules="loginRules" label-width="80px" label-position="left">
          <el-form-item label="用户名" prop="name">
            <el-input v-model="loginForm.name" placeholder="请输入用户名" prefix-icon=""></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input v-model="loginForm.password" placeholder="请输入密码" prefix-icon="" show-password></el-input>
          </el-form-item>
          <el-form-item label="面试码" prop="interview_code">
            <el-input v-model="loginForm.interview_code" placeholder="请输入面试码" prefix-icon=""></el-input>
          </el-form-item>
          <el-form-item label="登陆身份" prop="identity">
            <el-radio-group v-model="loginForm.identity" prop="identity">
              <el-radio label="user">求职者</el-radio>
              <el-radio label="admin">面试官</el-radio>
            </el-radio-group>
          </el-form-item>
        </el-form>
        <el-button class="login-button" @click="submitForm('loginForm')">登陆</el-button>
      </el-col>
    </el-row>

  </div>
</template>

<script>
    import {setCookie,getCookie} from "../assets/Cookie";

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
                this.$axios.post('/api/login/',JSON.stringify(this.loginForm)).then((res)=>{
                    console.log(res)
                    switch (res.data.loginMessage){
                        case 'success':
                            setCookie('name',this.loginForm.name)
                            setCookie('identity',this.loginForm.identity)
                            this.$router.push('/interview')
                            break
                        case 'no_user':
                            this.$message({
                                message:'用户名错误',
                                type:'error'
                            })
                            break
                        case 'wrong_password':
                            this.$message({
                                message:'密码错误',
                                type:'error'
                            })
                            break
                        case 'not_authorized':
                            this.$message({
                                message:'无权进入该面试场次',
                                type:'error'
                            })
                            break
                    }

                })
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
      },
      mounted(){
          if(getCookie('name')){
              if(getCookie('identity')=='user')
                  this.$router.push('/interview')
              else if(getCookie('identity')=='admin')
                  this.$router.push('/performance')
          }

      }

    }
</script>

<style scoped>
  .login-button{
    width: 100%;
  }
</style>
