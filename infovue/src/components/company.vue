<template>
    <div class="box">
        <div class="table1">
            <el-table :data="tableData1" class="el-table1" style="width: 100%" :cell-style="{ textAlign: 'center' }"
                :header-cell-style="{ 'text-align': 'center' }">
                <el-table-column label="2022年科技型中小企业清单">
                    <el-table-column v-for='item in  data_cloums' :key="item" :prop="item" :label="item" width="180" />
                </el-table-column>
            </el-table>
        </div>
        <div class="table2">
            <el-table :data="tableData2" class="el-table2" style="width: 100%" :cell-style="{ textAlign: 'center' }"
                :header-cell-style="{ 'text-align': 'center' }">
                <el-table-column label="园区有效期内高企清单">
                    <el-table-column v-for='item in  data_cloums' :key="item" :prop="item" :label="item" width="180" />
                </el-table-column>
            </el-table>
        </div>
    </div>
</template>

<script>
/* eslint-disable*/
export default {
    name: 'Companyp',
    data() {
        return {
            data_cloums: [
                "序号",
                "企业名称"
            ],
            tableData1: [],
            tableData2: []
        }
    },
    created() {
        this.$axios.get('/demo/company2')
            .then(res => {
                console.log(res.data)
                console.log(res.data["2022年科技型中小企业清单"])
                console.log(res.data["园区有效期内高企清单"])
                console.log(typeof (res.data))
                this.tableData1 = JSON.parse(res.data["2022年科技型中小企业清单"])
                this.tableData2 = JSON.parse(res.data["园区有效期内高企清单"])
                console.log(this.tableData1)
                console.log(this.tableData2)

            })
            .catch(err => {
                console.log(err)
            })
    }
}


</script>

<style scoped>
.box {
    width: 100%;
    display: flex;
 /*    border: 5px solid #00008B; */
    justify-content: center;
}

.table1 {

    margin: 10px;
}

.table2 {
    margin: 10px;
}

</style>