<template>
    <div>
        <NavBar></NavBar>
    </div>
</template>

<script>
    import {getCookie} from "../assets/Cookie";
    import NavBar from "../components/NavBar"

    export default {
        name: "AdminInstruction",
        components:{NavBar},
        created(){
            if(getCookie('identity') != 'admin'){
                this.$router.push('/login')
            }
        }
    }
</script>

<style scoped>

</style>