import Vue from 'vue'
import Router from 'vue-router'
import { constantRouterMap } from '@/config/router.config'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: '/',
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})
