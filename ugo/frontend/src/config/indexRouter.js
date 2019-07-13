// import { UserLayout, BasicLayout, RouteView, BlankLayout, PageView } from '@/views/layouts'

const indexRouterMap = [
  {
    path: '/',
    name: 'index',
    component: () => import('@/views/layouts/BasicLayout'),
    redirect: '/home',
    children: [
      {
        path: 'home',
        name: 'Home',
        component: () => import('@/views/home/index'),
        meta: { title: 'Home', keepAlive: true },
      }
    ]
  }
]

export default indexRouterMap