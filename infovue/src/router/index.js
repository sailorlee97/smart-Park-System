import Vue from 'vue'
import Router from 'vue-router'
import Homevue from '@/components/Homevue'
import Infovue from '@/components/Info'
import chanxuevue from '@/components/chanxue'
import companyinfovue from '@/components/companyinfo'
import companyvue from '@/components/company'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: Homevue
    },
    {
      path: '/Info',
      name: 'InfoPage',
      component: Infovue
    },
    {
      path: '/chanxue',
      name: 'chanxuePage',
      component: chanxuevue
    },
    {
      path: '/companyinfo',
      name: 'companyinfoPage',
      component: companyinfovue
    },
    {
      path: '/company',
      name: 'companyPage',
      component: companyvue
    }
  ]
})
