<template>
    <div>
        <NavBar></NavBar>
        <el-container>
            <el-aside>
                <el-menu @select="fetchPerson" :default-active="0">
                    <el-menu-item v-for="(p,index) in person" :index="index">
                        <span slot="title">{{p.name}}</span>
                    </el-menu-item>
                </el-menu>
            </el-aside>
            <el-main>
                <el-row :gutter="60">
                    <el-col :span="12">
                        <video class="p-video" autoplay controls src="/AI_Interview/video/101-jinguolin.mp4"></video>
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
        <!--<el-row>-->
            <!--<el-col :span="24">-->
                <!--<el-tabs tab-position="left" style="height: 100%;">-->
                    <!--<el-tab-pane v-for="p in person" :label="p.user_name">-->
                        <!--<el-row>-->
                            <!--<el-col :span="8" :offset="8">-->
                                <!--<video autoplay controls src="/Users/lawrence/pyprojects/AI_Interview/AI_Interview/video/101-caokaiyuan.mp4"></video>-->
                            <!--</el-col>-->
                        <!--</el-row>-->
                        <!--<el-row>-->
                            <!--<el-col :span="8" :offset="8">-->
                                <!--亲和力得分：{{p.grade}}-->
                            <!--</el-col>-->
                        <!--</el-row>-->
                    <!--</el-tab-pane>-->
                <!--</el-tabs>-->
            <!--</el-col>-->
        <!--</el-row>-->
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
                this.currentPerson.id=this.person[index].id
                this.currentPerson.name=this.person[index].name
                this.currentPerson.url=encodeURI(this.person[index].url)
                this.currentPerson.grade=this.person[index].grade
                this.currentPerson.admit=this.person[index].admit
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