<template>
    <div>
        <NavBar></NavBar>
        <el-row>
            <el-col :span="8" :offset="8">
                <download-excel :data="json_data" :fields="json_fields" name="list.xls">
                    <el-button  style="width: 100%;">导出名单</el-button>
                </download-excel>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import {getCookie} from "../assets/Cookie";
    import NavBar from "../components/NavBar";

    export default {
        name: "ExportExcel",
        components:{NavBar},
        data() {
            return {
                json_fields:{
                    "Name":"name",
                    "Telephone":"telephone",
                    "E-Mail":"email"
                },
                json_data:[
                ],
                json_meta: [
                    [{
                        'key': 'charset',
                        'value': 'utf-8'
                    }]
                ],
            }
        },
        methods:{
            getList(){
                this.$axios.get('api/getAdmit',{
                    params:{
                        content:getCookie('interview_code')
                    }
                }).then(res=>{
                    console.log(res)
                    if(res.data.code === 200){
                        if(res.data.data && res.data.data.length>0){
                            this.json_data=[]
                            let result = res.data.data
                            console.log(result)
                            for (let i in result){
                                let obj = {
                                    "name": result[i].fields.actual_name+"",
                                    "telephone": result[i].fields.telephone+"",
                                    "email": result[i].fields.email+"",
                                }
                                this.json_data.push(obj)
                            }
                            console.log(this.json_data)
                        }
                        else{
                            this.$message.error('No Data')
                        }
                    }
                    else{
                        this.$message.error(`Can't search database`)
                    }
                })
            }
        },
        created(){
            if(getCookie('identity') != 'admin'){
                this.$router.push('/login')
            }
            this.getList()
        }
    }
</script>

<style scoped>

</style>