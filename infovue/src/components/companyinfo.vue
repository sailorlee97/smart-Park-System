<template>
    <div class="staticdiv">
        <!-- <button @click="kuayu">"跨域请求"</button> -->
        <el-table :data="tableData"  style="width: 100%" >
    <el-table-column v-for='item in  data_cloums' :key="item" :prop="item" :label="item" width="181"/></el-table>
<!--         <el-table :data="tableData" stripe style="width: 100%">
            <el-table-column prop="序号" label="序号" width="180"> </el-table-column>
            <el-table-column prop="公司名称" label="公司名称" width="180"> </el-table-column>
            <el-table-column prop="成立日期" label="成立日期" width="180"> </el-table-column>
            <el-table-column prop="法定代表人" label="法定代表人" width="180"> </el-table-column>
            <el-table-column prop="注册资本" label="注册资本" width="180"> </el-table-column>
            <el-table-column prop="社会统一信用代码" label="社会统一信用代码" width="180"> </el-table-column>
            <el-table-column prop="电话" label="电话" width="180"> </el-table-column>
            <el-table-column prop="注册地址" label="注册地址" width="180"> </el-table-column>
            <el-table-column prop="经营范围" label="经营范围"> </el-table-column>
        </el-table> -->
    </div>
</template>

<script>
/* eslint-disable*/
export default {
    name: 'companyinfoP',
    data() {
        return {
            data_cloums:[
                "序号",
                "公司名称",
                "成立日期",
                "法定代表人",
                "注册资本",
                "统一社会信用代码",
                "电话",
                "注册地址",
                "经营范围"
            ],
            tableData:[]
 /*            tableData: [{ 
                xuhao: '1', 
                name: '南京辰极电子科技有限公司', 
                date: '2022-05-05', person: '李思远', 
                money: '500万人民币', xinyong: '91320106MABLK74U5E', 
                phone: '-', address: '南京市鼓楼区新模范马路66号物联网科技园大楼2层创业苗圃B区', 
                fanwei: '一般项目：技术服务、技术开发、技术咨询、技术交流、技术转让、技术推广；通信设备销售；电子测量仪器销售；移动通信设备销售；移动通信设备制造；通信设备制造；电子测量仪器制造（除依法须经批准的项目外，凭营业执照依法自主开展经营活动）' },
            { 
                xuhao: '2', 
                name: '南京柚智医云网络科技有限公司', 
                date: '2022-04-29', person: '吴珞铖', 
                money: '500万人民币', xinyong: '91320106MABM7JU249', 
                phone: '-', 
                address: '江苏省南京市鼓楼区新模范马路66号物联网科技园大楼2层创业苗圃B区', 
                fanwei: '一般项目：网络与信息安全软件开发；物联网技术研发；软件开发；网络技术服务；信息系统集成服务；信息技术咨询服务；计算机系统服务；数据处理服务；技术服务、技术开发、技术咨询、技术交流、技术转让、技术推广；企业管理咨询；会议及展览服务；专业设计服务；网络设备销售；互联网设备销售；电子产品销售；集成电路销售；软件销售；计算机软硬件及辅助设备零售（除依法须经批准的项目外，凭营业执照依法自主开展经营活动）' },
            {
                xuhao: '3', 
                name: '南京昱泉新能源科技有限公司', 
                date: '2022-04-06', 
                person: '解玲彬', 
                money: '160万人民币', 
                xinyong: '91320106MA7MJUJ06P', 
                phone: '-', 
                address: '南京市鼓楼区新模范马路66号物联网科技园大楼2层创业苗圃B区', 
                fanwei: '一般项目：新兴能源技术研发；海水淡化处理；太阳能发电技术服务；环保咨询服务；技术服务、技术开发、技术咨询、技术交流、技术转让、技术推广；其他文化艺术经纪代理；进出口代理；海洋工程装备销售；气体、液体分离及纯净设备销售；环境保护专用设备销售；太阳能热利用产品销售；光伏设备及元器件销售；太阳能热发电装备销售；海洋能系统与设备销售；玩具、动漫及游艺用品销售；光伏设备及元器件制造；新能源原动设备制造（除依法须经批准的项目外，凭营业执照依法自主开展经营活动）'
            }] */
        }
    },
/*     methods: { */
    created () {
      this.$axios.get('/demo/company1')
        .then(res => {
          this.tableData = JSON.parse(res.data)
          console.log(this.tableData)
          console.log(typeof(this.tableData))
        })
        .catch(err => {
          console.log(err)
        })
  }

}
</script>

<style scoped></style>