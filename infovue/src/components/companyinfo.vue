<template>
    <div class="box">
        <div class="col_news">
            <div class="col_news_head" frag="面板5">
                <ul class="col_metas clearfix" frag="窗口5" portletmode="simpleColumnAttri">

                    <li class="col_title">
                        <h2>学生创业企业</h2>
                    </li>
                    <li class="col_path"><span class="path_name">当前位置：</span><a href="http://localhost:8080/#/"
                            target="_self">首页</a><span class='possplit'>&nbsp;&nbsp;</span><a
                            href="http://localhost:8080/#/companyinfo" target="_self">学生创业企业</a></li>
                </ul>
            </div>
            <div class="col_news_con" frag="面板6">
                <div class="col_news_list" frag="窗口6" portletmode="simpleList">
                    <div class="wp_single wp_column_article" id="wp_column_article">
                        <div class="wp_entry">
                            <div class="wp_articlecontent">
                                <div id="wp_content_w6_0" class="paging_content" style="display:">
                                    <p>
                                        <br />
                                        <br />
                                    </p>
                                    <table class="MsoTableGrid" border="1" cellspacing="0" cellpadding="0"
                                        style="border:none;display: flex;">
                                        <tbody class="tabd">
                                            <tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:56px">
                                                <td width="64"
                                                    style="width:64px;border:solid #000 1px;mso-border-alt:solid #000 1px;background:#b6dde8;mso-background-themecolor:accent5;mso-background-themetint:102;padding:0cm 7px 0cm 7px;height:56px">
                                                    <p class="MsoNormal" style="text-align:center;text-align:center;">
                                                        <strong>
                                                            <span
                                                                style="font-size:16px;font-family:微软雅黑, sans-serif;">序号</span>
                                                        </strong>
                                                    </p>
                                                </td>
                                                <td width="406"
                                                    style="width:406px;border:solid #000 1px;border-left:none;mso-border-left-alt:solid #000 1px;mso-border-alt:solid #000 1px;background:#b6dde8;mso-background-themecolor:accent5;mso-background-themetint:102;padding:0cm 7px 0cm 7px;height:56px">
                                                    <p class="MsoNormal" style="text-align:center;text-align:center;">
                                                        <strong>
                                                            <span
                                                                style="font-size:16px;font-family:微软雅黑, sans-serif;">公司名称</span>
                                                        </strong>
                                                    </p>
                                                </td>
                                                <td width="406"
                                                    style="width:406px;border:solid #000 1px;border-left:none;mso-border-left-alt:solid #000 1px;mso-border-alt:solid #000 1px;background:#b6dde8;mso-background-themecolor:accent5;mso-background-themetint:102;padding:0cm 7px 0cm 7px;height:56px">
                                                    <p class="MsoNormal" style="text-align:center;text-align:center;">
                                                        <strong>
                                                            <span
                                                                style="font-size:16px;font-family:微软雅黑, sans-serif;">成立日期</span>
                                                        </strong>
                                                    </p>
                                                </td>
                                                <td width="406"
                                                    style="width:406px;border:solid #000 1px;border-left:none;mso-border-left-alt:solid #000 1px;mso-border-alt:solid #000 1px;background:#b6dde8;mso-background-themecolor:accent5;mso-background-themetint:102;padding:0cm 7px 0cm 7px;height:56px">
                                                    <p class="MsoNormal" style="text-align:center;text-align:center;">
                                                        <strong>
                                                            <span
                                                                style="font-size:16px;font-family:微软雅黑, sans-serif;">法定代表人</span>
                                                        </strong>
                                                    </p>
                                                </td>
                                                <td width="406"
                                                    style="width:406px;border:solid #000 1px;border-left:none;mso-border-left-alt:solid #000 1px;mso-border-alt:solid #000 1px;background:#b6dde8;mso-background-themecolor:accent5;mso-background-themetint:102;padding:0cm 7px 0cm 7px;height:56px">
                                                    <p class="MsoNormal" style="text-align:center;text-align:center;">
                                                        <strong>
                                                            <span
                                                                style="font-size:16px;font-family:微软雅黑, sans-serif;">经营范围</span>
                                                        </strong>
                                                    </p>
                                                </td>
                                            </tr>
                                            <tr v-for="(value, key) in  tableData" :key=key style="height:53px">
                                                <td width="64"
                                                    style="width:64px;border:solid #000 1px;border-top:none;mso-border-top-alt:solid #000 1px;mso-border-alt:solid #000 1px;padding:0cm 7px 0cm 7px;height:53px">
                                                    <p class="MsoNormal" style="text-align:center;text-align:center;">
                                                        <span lang="EN-US" style="font-size:15px;">{{ key + 1 }}</span>
                                                    </p>
                                                </td>
                                                <td width="406"
                                                    style="width:406px;border-top:none;border-left:none;border-bottom:solid #000 1px;border-right:solid #000 1px;mso-border-top-alt:solid #000 1px;mso-border-left-alt:solid #000 1px;mso-border-alt:solid #000 1px;padding:0cm 7px 0cm 7px;height:53px">
                                                    <p class="MsoNormal" style="text-align:center;text-align:center;">
                                                        <span style="font-size:16px;font-family:微软雅黑, sans-serif;">{{
                                                            value["公司名称"] }}</span>
                                                    </p>
                                                </td>
                                                <td width="406"
                                                    style="width:406px;border-top:none;border-left:none;border-bottom:solid #000 1px;border-right:solid #000 1px;mso-border-top-alt:solid #000 1px;mso-border-left-alt:solid #000 1px;mso-border-alt:solid #000 1px;padding:0cm 7px 0cm 7px;height:53px">
                                                    <p class="MsoNormal" style="text-align:center;text-align:center;">
                                                        <span style="font-size:16px;font-family:微软雅黑, sans-serif;">{{
                                                            value["成立日期"] }}</span>
                                                    </p>
                                                </td>
                                                <td width="406"
                                                    style="width:406px;border-top:none;border-left:none;border-bottom:solid #000 1px;border-right:solid #000 1px;mso-border-top-alt:solid #000 1px;mso-border-left-alt:solid #000 1px;mso-border-alt:solid #000 1px;padding:0cm 7px 0cm 7px;height:53px">
                                                    <p class="MsoNormal" style="text-align:center;text-align:center;">
                                                        <span style="font-size:16px;font-family:微软雅黑, sans-serif;">{{
                                                            value["法定代表人"] }}</span>
                                                    </p>
                                                </td>
                                                <td width="406"
                                                    style="width:406px;border-top:none;border-left:none;border-bottom:solid #000 1px;border-right:solid #000 1px;mso-border-top-alt:solid #000 1px;mso-border-left-alt:solid #000 1px;mso-border-alt:solid #000 1px;padding:0cm 7px 0cm 7px;height:53px">
                                                    <p class="MsoNormal" style="text-align:center;text-align:center;">
                                                        <span style="font-size:16px;font-family:微软雅黑, sans-serif;">{{
                                                            value["经营范围"] }}</span>
                                                    </p>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    <p>
                                        <br />
                                    </p>
                                    <p>
                                        <br />
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
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
            data_cloums: [
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
            tableData: []
        }
    },
    /*     methods: { */
    created() {
        this.$axios.get('/demo/company1')
            .then(res => {
                this.tableData = JSON.parse(res.data)
                console.log(this.tableData)
                console.log(typeof (this.tableData))
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
}
</style>