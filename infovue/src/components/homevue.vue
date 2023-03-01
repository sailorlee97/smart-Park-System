<template>
    <div id="home" class="Home">
        <table class="hometable">
            <tr>
                <th class="class1">
            <tr>
                <img  class="img1" src="../pictures/introduction.jpg">
            </tr>
            <tr>
                <a href="http://127.0.0.1/ny/#/" style="color:black; text-decoration: none;">园区概况</a>
            </tr>
            </th>
            <th class="class1">
                <tr>
                    <img  class="img1" src="../pictures/information.jpg">
                </tr>
                <tr>
                    <router-link to="/Info" style="color:black; text-decoration: none;">信息统计</router-link>
                </tr>
            </th>
            <th class="class1">
                <tr>
                    <img  class="img1" src="../pictures/company.jpg">
                </tr>
                <tr><router-link to="/company1" style="color:black; text-decoration: none;">企业</router-link></tr>
            </th>
            </tr>
            <tr>
                <th class="class1">
            <tr>
                <img  class="img1" src="../pictures/brain.jpg">
            </tr>
            <tr><router-link to="/companyinfo" style="color:black; text-decoration: none;">产业大脑</router-link></tr>
            </th>
            <th class="class1">
                <tr>
                    <img  class="img1" src="../pictures/police.jpg">
                </tr>
                <tr><router-link to="/keji" style="color:black; text-decoration: none;">科技动态</router-link></tr>
            </th>
            <th class="class1">
                <tr>
                    <img  class="img1" src="../pictures/chanxueyan.jpg">
                </tr>
                <tr><a href=" " style="color:black; text-decoration: none;">产学研合作</a></tr>
            </th>
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

.Home {
    width: 100%;
    height: 100%;
}

.img1{
    width:200px;
    height: 100px;
}
.class1 {
    font: 12px/1.5 Tahoma, Helvetica, Arial, '宋体', sans-serif;
    font-size: 35px;
    font-weight: 1000;
    color: black;
}

.hometable {
    border-spacing: 20px;
    height: 100%;
    width: 100%;
}
</style>