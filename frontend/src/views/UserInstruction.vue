<template>
    <div>
        <NavBar></NavBar>
        <el-row>
            <el-col :span="8" :offset="8">
                <div>
                    注意事项：
                </div>
                <div>
                    1. 请您在光线良好、环境安静的场所进行面试，尽量保证您肩膀以上的身体部位在摄像头录像范围内，这可能会对您的面试成绩造成影响。
                </div>
                <div>
                    2. 进入面试后，请您授权使用摄像头，否则将无法采集面试图像，这将极大影响您的面试成绩。
                </div>

                <div>
                    3. 在提示提交答案完成前，请您不要中途关闭浏览器，否则视频将有可能无法上传，这将极大影响您的面试成绩。
                </div>
                <div>
                    4. 进入面试后，您将有60秒的时间思考问题，300秒的时间进行作答，请合理使用时间。
                </div>
            </el-col>
            <el-col :span="8" :offset="8">
                <el-button  style="width: 100%;" @click="enter">进入面试</el-button>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import {getCookie} from "../assets/Cookie";
    import NavBar from "../components/NavBar"

    export default {
        name: "UserInstruction",
        components:{NavBar},
        methods:{
            enter(){
                this.$router.push('/interview')
            }
        },
        created() {
            if (getCookie('identity') != 'user') {
                this.$router.push('/login')
            }
        }
    }
</script>

<style scoped>

</style>