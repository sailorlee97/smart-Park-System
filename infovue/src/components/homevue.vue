<template>
<div class="zong">
    <div  class="home">
    <ul>
        <li class="span3" style="height: 300px;">
            <div class="thumbnail-style thumbnail-kenburn">
                <div class="thumbnail-img">
                    <div class="overflow-hidden"><img style="width: 260px;height: 160px;" src="../pictures/introduction.jpg" alt=""></div>
                    <!--<a class="btn-more hover-effect" href="/product/haoxinshu">查看详情</a>-->
                </div>
                <h3 title="园区概况" class=""><a href="http://127.0.0.1/ny/#/" style="color: #3498db;">园区概况</a></h3>
             </div>
        </li>
        <li class="span3" style="height: 300px;">
            <div class="thumbnail-style thumbnail-kenburn">
                <div class="thumbnail-img">
                    <div class="overflow-hidden"><img style="width: 260px;height: 160px;" src="../pictures/information.jpg" alt=""></div>
                    <!--<a class="btn-more hover-effect" href="/product/haoxinshu">查看详情</a>-->
                </div>
                <h3 title="信息统计" class=""><a href="http://localhost:8080/#/Info" style="color: #3498db;">信息统计</a></h3>
            </div>
        </li>
        <li class="span3" style="height: 300px;">
            <div class="thumbnail-style thumbnail-kenburn">
                <div class="thumbnail-img">
                    <div class="overflow-hidden"><img style="width: 260px;height: 160px;" src="../pictures/company.jpg" alt=""></div>
                    <!--<a class="btn-more hover-effect" href="/product/haoxinshu">查看详情</a>-->
                </div>
                <h3 title="企业" class=""><a href="http://localhost:8080/#/company1" style="color: #3498db;">企业</a></h3>
           </div>
        </li>
        </ul>
    </div>
    <div  class="home">
        <ul>
        <li class="span3" style="height: 0px;">
            <div class="thumbnail-style thumbnail-kenburn">
                <div class="thumbnail-img">
                    <div class="overflow-hidden"><img style="width: 260px;height: 160px;" src="../pictures/brain.jpg" alt=""></div>
                    <!--<a class="btn-more hover-effect" href="/product/homecare">查看详情</a>-->
                </div>
                <h3 title="产业大脑" class=""><a href="http://localhost:8080/#/companyinfo" style="color: #3498db;">产业大脑</a></h3>
            </div>
        </li>
        <li class="span3" style="height: 0px;">
            <div class="thumbnail-style thumbnail-kenburn">
                <div class="thumbnail-img">
                    <div class="overflow-hidden"><img style="width: 260px;height: 160px;" src="../pictures/police.jpg" alt=""></div>
                    <!--<a class="btn-more hover-effect" href="/product/telemed">查看详情</a>-->
                </div>
                <h3 title="科技动态" class=""><a  href="http://localhost:8080/#/keji" style="color: #3498db;">科技动态</a></h3>
           </div>
        </li>
        <li class="span3" style="height: 0px;">
            <div class="thumbnail-style thumbnail-kenburn">
                <div class="thumbnail-img">
                    <div class="overflow-hidden"><img style="width: 260px;height: 160px;" src="../pictures/chanxueyan.jpg" alt=""></div>
                    <!--<a class="btn-more hover-effect" href="/product/chronic">查看详情</a>-->
                </div>
                <h3 title="产学研合作" class=""><a style="color: #3498db;">产学研合作</a></h3>
            </div>
        </li>
    </ul>
</div>
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

<style scoped>
@import '../../_css/style.css';
@import '../../_css/bootstrap.min.css';
@import '../../_css/bootstrap-responsive.min.css';

@import '../../_css/fonts.css';

.home{
    display: flex;
    justify-content: center
}
</style>