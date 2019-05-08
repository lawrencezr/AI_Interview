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
                <el-button @click="submitAnswer()">结束作答</el-button>
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
                recorder: null
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
                this.recorder.stopRecording(this.stopRecordingCallback)
                if(this.activeStep == 3)
                    this.$router.push('/interview_end')
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
                let blob = new Blob(recordedBlobs,{type: 'video/mp4'})
                let file = new File([blob],)
                this.video.src = URL.createObjectURL((this.recorder.getBlob()))
                window.open(URL.createObjectURL(this.recorder.getBlob()))
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