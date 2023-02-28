<template>
    <div class="wrapper" id="container">
        <div class="inner">
            <div class="col_menu">
                <div class="col_menu_head" frag="面板3">
                    <h3 class="col_name" frag="窗口3" portletmode="simpleColumnAnchor">
                        <span class="col_name_text">
                            <span class='Column_Anchor'>企业</span>
                        </span>
                    </h3>
                </div>
                <div class="col_menu_con" frag="面板4">
                    <div class="col_list" frag="窗口4" portletmode="simpleColumnList">
                        <div id="wp_listcolumn_w4">

                            <ul class="wp_listcolumn">

                                <li class="wp_column column-1 ">
                                    <a href="http://127.0.0.1:8080/#/company1" title="2022年科技型中小企业清单" class="" target="_self"><span
                                            class="column-name">2022年科技型中小企业清单</span></a>
                                </li>

                                <li class="wp_column column-2 selected">
                                    <a href="http://127.0.0.1:8080/#/company2" title="2022年科技型中小企业清单" class="selected" target="_self"><span
                                            class="column-name">园区有效期内高企清单</span></a>
                                </li>
                            </ul>

                        </div>
                    </div>
                </div>
            </div>
            <div class="col_news">
                <div class="col_news_head" frag="面板5">
                    <ul class="col_metas clearfix" frag="窗口5" portletmode="simpleColumnAttri">

                        <li class="col_title">
                            <h2>园区有效期内高企清单</h2>
                        </li>
                        <li class="col_path"><span class="path_name">当前位置：</span><a href="http://127.0.0.1:8080/#/"
                                target="_self">首页</a><span class='possplit'>&nbsp;&nbsp;</span><a href="http://127.0.0.1:8080/#/company1"
                                target="_self">企业</a><span class='possplit'>&nbsp;&nbsp;</span><a href="http://127.0.0.1:8080/#/company2"
                                target="_self">园区有效期内高企清单</a></li>
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
                                                                    style="font-size:16px;font-family:微软雅黑, sans-serif;">企业名称</span>
                                                            </strong>
                                                        </p>
                                                    </td>
                                                </tr>
                                                <tr v-for="(value, key) in tableData2" :key=key style="height:53px">
                                                    <td width="64"
                                                        style="width:64px;border:solid #000 1px;border-top:none;mso-border-top-alt:solid #000 1px;mso-border-alt:solid #000 1px;padding:0cm 7px 0cm 7px;height:53px">
                                                        <p class="MsoNormal" style="text-align:center;text-align:center;">
                                                            <span lang="EN-US" style="font-size:15px;">{{ key+1 }}</span>
                                                        </p>
                                                    </td>
                                                    <td width="406"
                                                        style="width:406px;border-top:none;border-left:none;border-bottom:solid #000 1px;border-right:solid #000 1px;mso-border-top-alt:solid #000 1px;mso-border-left-alt:solid #000 1px;mso-border-alt:solid #000 1px;padding:0cm 7px 0cm 7px;height:53px">
                                                        <p class="MsoNormal" style="text-align:center;text-align:center;">
                                                            <span
                                                                style="font-size:16px;font-family:微软雅黑, sans-serif;">{{ value["企业名称"] }}</span>
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
            <div class="clear"></div>
        </div>
    </div>
</template>

<script>
/* eslint-disable*/
export default {
    name: 'Companyp2',
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
.tabd{
    margin: auto;
}
/* .table_box{
    display: flex;
}
.table1{
    margin: auto;
} */</style>