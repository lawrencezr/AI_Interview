<template>
    <div>
        <NavBar></NavBar>
        <el-row :gutter="20" v-for="(t,index) in train">
            <el-col :span="6">
                <video class="p-video" controls :src="t[0].url"></video>
                <el-input v-model="trainForm['q'+t[0].id]" placeholder="请输入评分"></el-input>
            </el-col>
            <el-col :span="6">
                <video class="p-video" controls :src="t[1].url"></video>
                <el-input v-model="trainForm['q'+t[1].id]"  placeholder="请输入评分"></el-input>
            </el-col>
            <el-col :span="6">
                <video class="p-video" controls :src="t[2].url"></video>
                <el-input v-model="trainForm['q'+t[2].id]" placeholder="请输入评分"></el-input>
            </el-col>
            <el-col :span="6">
                <video class="p-video" controls :src="t[3].url"></video>
                <el-input v-model="trainForm['q'+t[3].id]" placeholder="请输入评分"></el-input>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="8" :offset="8">
                <el-button @click="submitScore()" style="width: 100%;">提交分数</el-button>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import NavBar from '../components/NavBar.vue'
    import {getCookie} from "../assets/Cookie";

    export default {
        name: "Train",
        components : {NavBar},
        data(){
            return{
               trainForm:{},
                train:[],
            }
        },
        methods:{
            getTrain(){
                this.$axios.get('api/getTrain',{
                    params: {
                        content: getCookie('interview_code')
                    }
                }).then(res=>{
                    if(res.data.code === 200){
                        if(res.data.data && JSON.parse(res.data.data).length>0){
                            this.train=[]
                            let result = JSON.parse(res.data.data)
                            let count = -1
                            console.log(result)
                            for (let i in result){
                                let obj = {
                                    id: result[i].pk,
                                    url: result[i].fields.url,
                                }
                                if(i % 4==0){
                                    count++
                                    this.train.push([])
                                    this.train[count].push(obj)
                                }
                                else{
                                    this.train[count].push(obj)
                                }
                            }
                            console.log(this.train)
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
            submitScore(){
                console.log(this.trainForm)
                this.$axios.post('/api/setTrain/',JSON.stringify(this.trainForm)).then(res=>{
                    if(res.data.code == 200){
                        this.$message.success('打分成功！')
                    }
                    else{
                        this.$message.error('打分失败！请重试！')
                    }
                })

            }
        },
        created(){
            if(getCookie('identity') != 'admin'){
                this.$router.push('/login')
            }
        },
        mounted(){
            this.getTrain()
        }
    }
</script>

<style scoped>
    .el-row{
        margin-bottom: 20px;
    }
.p-video{
    height: 125.06px;
    width:  222px;
}
</style>