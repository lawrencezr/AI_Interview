<template>
    <div>
        <NavBar></NavBar>
        <el-container>
            <el-aside>
                <el-menu @select="fetchPerson" default-active="0">
                    <el-menu-item v-for="(p,index) in person" :index="index.toString()">
                        <span slot="title">{{p.name}}</span>
                    </el-menu-item>
                </el-menu>
            </el-aside>
            <el-main>
                <el-row :gutter="60">
                    <el-col :span="12">
                        <video id="pvideo" class="p-video" autoplay controls :src="currentPerson.url">
                        </video>
                    </el-col>
                    <el-col :span="12">
                        <el-row>
                            <el-col :span="24">姓名： {{currentPerson.name}}</el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="24">亲和力得分： {{currentPerson.grade}}</el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="24">
                                <el-button v-if="currentPerson.admit == false" type="success">合格</el-button>
                            </el-col>
                            <el-col :span="24">
                                <el-button v-if="currentPerson.admit == true" type="danger">不合格</el-button>
                            </el-col>
                        </el-row>
                    </el-col>
                </el-row>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    import {getCookie} from "../assets/Cookie";
    import NavBar from "../components/NavBar"

    export default {
        name: "Performance",
        components:{NavBar},
        data(){
          return{
              person:[],
              currentPerson:{
                  id:0,
                  name:'',
                  grade:0,
                  url:'',
                  admit:false
              }
          }
        },
        methods: {
            getAffinity(){
                this.$axios.get('api/getAffinity',{
                    params: {
                        content: getCookie('interview_code')
                    }
                }).then(res=>{
                    if(res.data.code === 200){
                        if(res.data.data && JSON.parse(res.data.data).length>0){
                            this.person=[]
                            let result = JSON.parse(res.data.data)
                            for (let i in result){
                                let obj = {
                                    id: result[i].pk,
                                    name: result[i].fields.user_name,
                                    grade: Number(result[i].fields.grade),
                                    url: result[i].fields.url,
                                    admit: result[i].fields.admit
                                }
                                this.person.push(obj)
                            }
                            console.log(this.person)
                        }
                        else{
                            this.$message.error('No Data')
                        }
                    }
                    else{
                        this.$message.error(`Can't search database`)
                    }
                })
            },
            fetchPerson(index){
                let i = parseInt(index)
                this.currentPerson.id=this.person[i].id
                this.currentPerson.name=this.person[i].name
                this.currentPerson.url=this.person[i].url
                this.currentPerson.grade=this.person[i].grade
                this.currentPerson.admit=this.person[i].admit
            }
        },
        created(){
            if(getCookie('identity') != 'admin'){
                this.$router.push('/login')
            }
            this.getAffinity()
        }
    }
</script>

<style scoped>
    .el-row{
        margin-bottom: 20px;
    }
.p-video{
    height: 100%;
    width: 100%;
}
</style>