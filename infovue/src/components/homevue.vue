<template>
    <div id="home">
   <!--      <div id="com-tab">
            <ul class="wp_nav">
                <li class="item1">
                    <a href="http://127.0.0.1/ny/#/" style="color:black; text-decoration: none;"><span
                            class="园区概况">园区概况</span></a>
                    <i class="mark"></i>
                </li>
                <li class="item1">
                    <router-link to="/Info" style="color:black; text-decoration: none;"><span
                            class="信息统计">信息统计</span></router-link>
                    <i class="mark"></i>
                </li>
            </ul>
        </div> -->
 <!--    </div> -->
        <!-- <div class="bg" :style="background"> -->
        <table class="hometable">
            <tr>
                <th class="class1"><a href="http://127.0.0.1/ny/#/" style="color:black; text-decoration: none;">园区概况</a>
                </th>
                <th class="class1"><router-link to="/Info" style="color:black; text-decoration: none;">信息统计</router-link>
                </th>
                <th class="class1">
                    <router-link to="/company" style="color:black; text-decoration: none;">企业</router-link>
                </th>
            </tr>
            <tr>
                <th class="class1"><router-link to="/companyinfo"
                        style="color:black; text-decoration: none;">产业大脑</router-link></th>
                <th class="class1"><router-link to="/chanxue"
                        style="color:black; text-decoration: none;">产学研合作</router-link></th>
                <th class="class1"><a href=" " style="color:black; text-decoration: none;">科技动态</a></th>
            </tr>
        </table>
    </div>
</template>

<script>
/* eslint-disable*/
export default {
    name: 'Homepage',
    data() {
        return {
            background: {
                // 背景图片地址
                backgroundImage: 'url(' + require('../assets/img2.png') + ')',
            }
        }
    }
}
</script>

<style type="text/css">
/* .bg{
    width:100%;  
    height:100%;  
    z-index:-1;
    position: absolute;
} */

.class1 {
    font: 12px/1.5 Tahoma, Helvetica, Arial, '宋体', sans-serif;
    font-size: 35px;
    font-weight: 1000;
    color: black;
    border: solid;
    border-width: thick;
    border-style: outset;
    border-collapse: separate;

}

.hometable {
    margin: 0 auto;
    border-spacing: 100px;
    height: 20%
}
</style>