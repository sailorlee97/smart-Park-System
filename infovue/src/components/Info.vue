<template>
  <div class="info">
    <button @click="drawLine">"load-data"</button>
    <div class="HelloWorld echart-box" id="myChart1" :style="{ width: '1000px', height: '500px', background: '#ffffff' }">
    </div>
    <!--     <button @click="kuayu">"跨域请求"</button>
    <table >
      <tr v-for="(value, key) in list" :key=key>
        <td>{{ key }} - {{ value }}</td>
      </tr>
    </table> -->
  </div>
</template>

<script>
/* eslint-disable*/
export default {
  name: 'InfoP',
  data() {
    return {
      datas: [],
      pieName: ["Teacher", "Staff", "Student"],
    }
  },
 created() {
    this.$axios.get('/demo/json')
      .then(res => {
        console.log(res);
        this.datas=res.data
        /*      this.datas = res.data
             console.log(res.data) */
      })
      .catch(err => {
        console.log(err)
        alert("No data get!")
      })
  },
/*   mounted() {
    console.log(this.datas);
    this.drawLine();
  }, */
  methods: {
    drawLine() {
      this.$axios.get('/demo/json')
      .then(res => {
        console.log(res);
        this.datas=res.data
        /*      this.datas = res.data
             console.log(res.data) */
      })
      .catch(err => {
        console.log(err)
        alert("No data get!")
      })
      // 1、基于准备好的dom，初始化echarts实例
      let myChart = this.$echarts.init(document.getElementById("myChart1"));
      //2、构造图表数据
      let options = {
        title: {
          text: "进出情况",
          left: "center",
        },
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ({d}%)",
        },
        legend: {
          orient: "vertical",
          left: "left",
          data: this.pieName,
        },
        series: [
          {
            name: "访问来源",
            type: "pie",
            radius: "55%",
            center: ["50%", "60%"],
            data: this.datas,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
            },
          },
        ],
      };
      // 3、绘制图表
      myChart.setOption(options);
    }
  }

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


</script>

<style scoped></style>
