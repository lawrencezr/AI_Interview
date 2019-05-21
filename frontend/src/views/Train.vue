<template>
    <div>
        <NavBar></NavBar>
        <el-row :gutter="20">
            <el-col :span="6">
                <video class="p-video" controls src="../../../AI_Interview/video/101-chengkaiwei.mp4"></video>
                <el-input v-model="trainForm.q1" placeholder="请输入评分"></el-input>
            </el-col>
            <el-col :span="6">
                <video class="p-video" controls src="../../../AI_Interview/video/101-caokaiyuan.mp4"></video>
                <el-input v-model="trainForm.q2" placeholder="请输入评分"></el-input>
            </el-col>
            <el-col :span="6">
                <video class="p-video" controls src="../../../AI_Interview/video/101-fanpeng.mp4"></video>
                <el-input v-model="trainForm.q3" placeholder="请输入评分"></el-input>
            </el-col>
            <el-col :span="6">
                <video class="p-video" controls src="../../../AI_Interview/video/101-lusunhanyan.mp4"></video>
                <el-input v-model="trainForm.q4" placeholder="请输入评分"></el-input>
            </el-col>
        </el-row>
        <el-row :gutter="20">
            <el-col :span="6">
                <video class="p-video" controls src="../../../AI_Interview/video/101-taojiacheng.mp4"></video>
                <el-input v-model="trainForm.q5" placeholder="请输入评分"></el-input>
            </el-col>
            <el-col :span="6">
                <video class="p-video" controls src="../../../AI_Interview/video/101-zhangyujie.mp4"></video>
                <el-input v-model="trainForm.q6" placeholder="请输入评分"></el-input>
            </el-col>
            <el-col :span="6">
                <video class="p-video" controls src="../../../AI_Interview/video/101-sunlichen.mp4"></video>
                <el-input v-model="trainForm.q7" placeholder="请输入评分"></el-input>
            </el-col>
            <el-col :span="6">
                <video class="p-video" controls src="../../../AI_Interview/video/101-dudanyang.mp4"></video>
                <el-input v-model="trainForm.q8" placeholder="请输入评分"></el-input>
            </el-col>
        </el-row>
        <el-row :gutter="20">
            <el-col :span="6">
                <video class="p-video" controls src="../../../AI_Interview/video/101-jiangyuanpeng.mp4"></video>
                <el-input v-model="trainForm.q9" placeholder="请输入评分"></el-input>
            </el-col>
            <el-col :span="6">
                <video class="p-video" controls src="../../../AI_Interview/video/101-yangjiaxin.mp4"></video>
                <el-input v-model="trainForm.q10" placeholder="请输入评分"></el-input>
            </el-col>
            <el-col :span="6">
                <video class="p-video" controls src="../../../AI_Interview/video/101-wangwencan.mp4"></video>
                <el-input v-model="trainForm.q11" placeholder="请输入评分"></el-input>
            </el-col>
            <el-col :span="6">
                <video class="p-video" controls src="../../../AI_Interview/video/101-wangjingbo.mp4"></video>
                <el-input v-model="trainForm.q12" placeholder="请输入评分"></el-input>
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
               trainForm:{}
            }
        },
        created(){
            if(getCookie('identity') != 'admin'){
                this.$router.push('/login')
            }
        },
    }
</script>

<style scoped>
    .el-row{
        margin-bottom: 20px;
    }
.p-video{
    height: 100%;
    width:  100%;
}
</style>