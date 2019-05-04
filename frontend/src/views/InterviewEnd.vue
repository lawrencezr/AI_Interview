<template>
    <div>
        <el-row>
            <el-col :span="24"><NavBar></NavBar></el-col>
        </el-row>
        <el-row>
            <el-col :span="12" :offset="6">考试结束，感谢使用！</el-col>
        </el-row>
    </div>
</template>

<script>
    import NavBar from '../components/NavBar.vue'
    import {getCookie} from "../assets/Cookie";

    export default {
        name: "InterviewEnd",
        components : {NavBar},
        created(){
            if(getCookie('identity') != 'user'){
                this.$router.push('/login')
            }
        },
    }
</script>

<style scoped>

</style>