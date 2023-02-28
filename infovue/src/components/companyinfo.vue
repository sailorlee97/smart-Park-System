<template>
    <div class="box">
     <div class="col_news">
        <div class="col_news_head" frag="面板5">
            <ul class="col_metas clearfix" frag="窗口5" portletmode="simpleColumnAttri">

                <li class="col_title">
                    <h2>产业大脑</h2>
                </li>
                <li class="col_path"><span class="path_name">当前位置：</span><a href="http://127.0.0.1:8080/#/"
                        target="_self">首页</a><span class='possplit'>&nbsp;&nbsp;</span><a
                        href="http://127.0.0.1:8080/#/companyinfo" target="_self">产业大脑</a></li>
            </ul>
        </div>
    <div class="staticdiv">
        <!-- <button @click="kuayu">"跨域请求"</button> -->
        <el-table :data="tableData"  style="width: 100%" >
    <el-table-column v-for='item in  data_cloums' :key="item" :prop="item" :label="item" width="181"/></el-table>
    </div>
</div>
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

<style scoped>
.box {
    width: 100%;
    display: flex;
    justify-content: center
}</style>