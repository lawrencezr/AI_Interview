<template>
    <div>
        <el-row>
            <el-col :span="24"><NavBar></NavBar></el-col>
        </el-row>
        <el-row>
            <el-col :span="24">面试界面</el-col>
        </el-row>
    </div>
</template>

<script>
    import {getCookie} from "../assets/Cookie";
    import NavBar from "../components/NavBar"

    export default {
        name: "Interview",
        components:{NavBar},
        created(){
            if(getCookie('identity') != 'user'){
                this.$router.push('/login')
            }
        }
    }
</script>

<style scoped>

</style>