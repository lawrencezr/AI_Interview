<template>
    <div>
        成绩界面
    </div>
</template>

<script>
    import {getCookie} from "../assets/Cookie";
    export default {
        name: "Performance",
        created(){
            if(getCookie('identity') != 'admin'){
                this.$router.push('/login')
            }
        }
    }
</script>

<style scoped>

</style>