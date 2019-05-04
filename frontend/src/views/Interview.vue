<template>
    <div class="question">
        <el-row>
            <el-col :span="24"><NavBar></NavBar></el-col>
        </el-row>
        <el-row>
            <el-col :span="12" :offset="6">
                <el-steps :active="activeStep" finish-status="success">
                    <el-step title="问题 1"></el-step>
                    <el-step title="问题 2"></el-step>
                    <el-step title="问题 3"></el-step>
                </el-steps>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="12" :offset="6">
                <el-progress :stroke-width="18" :percentage="percentage" status="text">
                    {{timeLeft}}s
                </el-progress>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="12" :offset="6">
                {{question}}
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="12" :offset="6">

            </el-col>
        </el-row>
        <el-row v-if="isPrepare">
            <el-col :span="12" :offset="6">
                <el-button @click="startAnswer()">开始作答</el-button>
            </el-col>
        </el-row>
        <el-row v-if="!isPrepare">
            <el-col :span="12" :offset="6">
                <el-button @click="submitAnswer()">结束作答</el-button>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import {getCookie} from "../assets/Cookie";
    import NavBar from "../components/NavBar"

    export default {
        name: "Interview",
        components:{NavBar},
        data(){
            return{
                activeStep:0,
                percentage:100,
                timeLeft:0,
                timeSum:0,
                isPrepare: true,
                question: '1. 请介绍一下自己。（你将有60秒的时间进行思考，300秒的时间进行作答）'
            };
        },
        methods:{
            countDown() {
                this.timeLeft--
                this.percentage = this.timeLeft/this.timeSum*100
                if(this.timeLeft == 0 && this.timeSum == 60){
                    this.startAnswer()
                }
                else if(this.timeLeft == 0 && this.timeSum == 300){
                    this.submitAnswer()
                }
            },
            startAnswer(){
                this.isPrepare = false
                this.timeLeft = 300
                this.timeSum = 300
                this.$message({
                    message:'开始作答'
                })
            },
            submitAnswer(){
                this.$message({
                    message:'答案已提交'
                })
                this.isPrepare = true
                this.timeLeft = 60
                this.timeSum = 60
                if(this.activeStep++ > 2) this.activeStep = 0
                console.log(this.activeStep)
                if(this.activeStep == 3)
                    this.$router.push('/interview_end')
            }
        },
        created(){
            if(getCookie('identity') != 'user'){
                this.$router.push('/login')
            }
        },
        mounted(){
            if(this.isPrepare){
                this.timeLeft = 60
                this.timeSum = 60
            }
            else {
                this.timeLeft = 300
                this.timeSum = 300
            }
            setInterval(this.countDown,1000)

        }
    }
</script>

<style scoped>
    .el-row{
        margin-bottom: 10px;
    }
    .el-button{
        width:100%;
    }
</style>