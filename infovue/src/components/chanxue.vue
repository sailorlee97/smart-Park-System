<template>
    <div class="box">
    <div class="col_news">
        <div class="col_news_head" frag="面板5">
            <ul class="col_metas clearfix" frag="窗口5" portletmode="simpleColumnAttri">

                <li class="col_title">
                    <h2>产学研合作</h2>
                </li>
                <li class="col_path"><span class="path_name">当前位置：</span><a href="http://127.0.0.1:8080/#/"
                        target="_self">首页</a><span class='possplit'>&nbsp;&nbsp;</span><a
                        href="http://127.0.0.1:8080/#/chanxue" target="_self">产学研合作</a></li>
            </ul>
        </div>
        <div class="col_news_con" frag="面板6">
            <div class="col_news_list" frag="窗口6" portletmode="simpleList">
                <div id="wp_news_w6">

                    <ul class="wp_article_list"  v-for="(value, key) in list" :key=key>

                        <li class="list_item i1">
                            <div class="fields pr_fields">
                                <span class='Article_Index'>{{ key+1 }}</span>
                                <span class='Article_Title'><a
                                        :href="value['url']"
                                        target='_blank'
                                        title='关于下达2018年度第二批省级工业和信息产业转型升级专项资金指标的通知'>{{ value['title'] }}</a></span>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
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
  
<style scoped>.box {
    width: 100%;
    display: flex;
    justify-content: center
}</style>
  