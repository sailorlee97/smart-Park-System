// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import ElementUI from 'element-ui'
import * as echarts from 'echarts'
import 'element-ui/lib/theme-chalk/index.css'
import '../_upload/tpl/02/5d/605/template605/base.css'
import '../_upload/tpl/02/5d/605/template605/listdis.css'
import '../_js/_portletPlugs/simpleNews/css/simplenews.css'
import '../_js/_portletPlugs/sudyNavi/css/sudyNav.css'
Vue.use(ElementUI)
Vue.config.productionTip = false
Vue.prototype.$echarts = echarts
Vue.prototype.$axios = axios

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
