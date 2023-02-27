<template>
<div class="box">
    <div class="chanxue">
        <el-table :data="list" style="width: 100%" :cell-style="{ textAlign: 'center' }"
            :header-cell-style="{ 'text-align': 'center' }">
            <el-table-column prop="title" label="标题" width="180" />
            <el-table-column prop="url" label="域名" width="180"></el-table-column>
        </el-table>
    </div>
</div>
</template>

<script>
/* eslint-disable*/
export default {
    name: 'Chanxuep',
    data() {
        return {
            list: []
        }
    },
    created() {
        this.$axios.get('/demo/asin')
            .then(res => {
                this.list = res.data
                console.log(res.data)
            })
            .catch(err => {
                console.log(err)
                alert("No data get!")
            })
    }
    /*   created() {
        axios.get('/demo/json')
          .then(res => {
            this.list = res
            console.log(res)
          })
          .catch(err => {
            console.log(err)
          })
      } */

}
</script>
  
<style scoped>
.box{
    width: 100%;
    display: flex;
    justify-content: center
}
</style>
  