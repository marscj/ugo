import { UserLayout, BasicLayout, RouteView, BlankLayout, PageView } from '@/view/layouts'

export const indexRouterMap = [
  {
    path: '/',
    name: 'index',
    component: BasicLayout,
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