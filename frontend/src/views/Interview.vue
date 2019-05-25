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
                <video class="camera-video" autoplay ref="video"></video>
            </el-col>
        </el-row>
        <el-row v-if="isPrepare">
            <el-col :span="12" :offset="6">
                <el-button @click="startAnswer()">开始作答</el-button>
            </el-col>
        </el-row>
        <el-row v-if="!isPrepare">
            <el-col :span="12" :offset="6">
                <el-button v-if="activeStep<2" @click="pauseAnswer()">结束作答</el-button>
                <el-button v-if="activeStep==2" @click="submitAnswer()">提交答案</el-button>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import {getCookie} from "../assets/Cookie";
    import NavBar from "../components/NavBar"
    import RecordRTC from 'recordrtc'

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
                question: '1. 请介绍一下自己。（你将有60秒的时间进行思考，300秒的时间进行作答）',
                video: null,
                recorder: null,
                isOver : false
            };
        },
        methods:{
            countDown() {
                this.timeLeft--
                this.percentage = this.timeLeft/this.timeSum*100
                if(this.timeLeft == 0 && this.timeSum == 60){
                    this.startAnswer()
                }
                else if(this.timeLeft == 0 && this.timeSum == 300 && this.activeStep<2){
                    this.pauseAnswer()
                }
                else if(this.timeLeft == 0 && this.timeSum == 300 && this.activeStep==2){
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
                if(this.activeStep==0){
                    this.captureCamera((camera)=>{
                    this.video.muted=true
                    this.video.volume=0;
                    this.video.srcObject=camera
                    this.recorder = RecordRTC(camera,{
                        type:'video',
                        mimeType:'video/webm;codecs=h264'
                    })
                    this.recorder.startRecording()
                    this.recorder.camera=camera
                })
                }
                else{
                    this.recorder.resumeRecording()
                }

            },
            pauseAnswer(){
                this.isPrepare = true
                this.timeLeft = 60
                this.timeSum = 60
                this.recorder.pauseRecording()
                this.activeStep++
            },
            submitAnswer(){
                // this.isPrepare = true
                // this.timeLeft = 60
                // this.timeSum = 60
                //if(this.activeStep > 2) this.activeStep = 0
                console.log(this.activeStep)
                this.isOver=true
                this.recorder.stopRecording(this.stopRecordingCallback)

            },
            captureCamera(callback){
                navigator.mediaDevices.getUserMedia({audio:true,video:true}).then(function(camera){
                    callback(camera)
                }).catch((error)=>{
                    this.$message.error('未找到视频设备')
                })
            },
            stopRecordingCallback(){
                this.video.src = this.video.srcObject = null
                this.video.muted = false
                this.video.volume = 1;
                let recordedBlobs = this.recorder.getBlob()
                var file = new File([recordedBlobs],getCookie('interview_code')+'-'+getCookie('name')+'.webm',{type:'video/webm'})
                var formData = new FormData()
                formData.append('video',file)
                formData.append('name',getCookie('name'))
                formData.append('interview_code',getCookie('interview_code'))
                var request = new XMLHttpRequest()
                var url = 'http://127.0.0.1:8000/api/uploadVideo/'
                request.open("POST",url)
                request.send(formData)
                const loading =this.$loading({
                    lock:true,
                    text:'Uploading',
                    spinner:'el-icon-loading',
                    background:'rgba(0,0,0,0.7)'
                })
                let self = this
                request.onreadystatechange=function () {
                    var res = request.responseText
                    if (request.readyState == 4 && request.status==200){
                        res = JSON.parse(res)
                        console.log(res)
                        if(res['code']== 200){
                            loading.close()
                            self.$message({
                                message:'视频已提交'
                            })
                            self.$router.push('/interview_end')
                        }
                        // else if(res.data.code == '0'){
                        //     request.open("POST",url)
                        //     request.send(formData)
                        // }
                    }
                    // else{
                    //     request.open("POST",url)
                    //     request.send(formData)
                    // }
                }
                this.recorder.camera.stop()
                this.recorder.destroy()
                this.recorder = null
            }
        },
        created(){
            if(getCookie('identity') != 'user'){
                this.$router.push('/login')
            }
            this.captureCamera((camera)=>{
                    this.video.muted=true
                    this.video.volume=0;
                    this.video.srcObject=camera})
        },
        mounted(){
            this.video = document.querySelector('video')
            if(this.isPrepare){
                this.timeLeft = 60
                this.timeSum = 60
            }
            else {
                this.timeLeft = 300
                this.timeSum = 300
            }
            if(this.isOver == false)
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
    .camera-video{
        height:100%;
        width:100%;
    }
</style>