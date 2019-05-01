<template>
    <div>面试界面</div>
</template>

<script>
    import {getCookie} from "../assets/Cookie";

    export default {
        name: "Interview",
        created(){
            if(getCookie('identity') != 'user'){
                this.$router.push('/login')
            }
        }
    }
</script>

<style scoped>

</style>