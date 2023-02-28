import Vue from 'vue'
import Router from 'vue-router'
import Homevue from '@/components/Homevue'
import Infovue from '@/components/Info'
import kejivue from '@/components/keji'
import companyinfovue from '@/components/companyinfo'
import companyvue1 from '@/components/company1'
import companyvue2 from '@/components/company2'
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
      path: '/keji',
      name: 'kejiPage',
      component: kejivue
    },
    {
      path: '/companyinfo',
      name: 'companyinfoPage',
      component: companyinfovue
    },
    {
      path: '/company1',
      name: 'companyPage1',
      component: companyvue1
    },
    {
      path: '/company2',
      name: 'companyPage2',
      component: companyvue2
    }
  ]
})
