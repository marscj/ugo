import { UserLayout, BasicLayout, RouteView, BlankLayout, PageView } from '@/layouts'
import { bxAnaalyse } from '@/core/icons'

export const asyncRouterMap = [
  {
    path: '/admin',
    name: 'admin',
    component: BasicLayout,
    meta: { title: 'Dashboard' },
    redirect: '/admin/dashboard',
    children: [
      // dashboard
      {
        path: 'dashboard',
        name: 'dashboard',
        redirect: '/admin/dashboard/workplace',
        component: RouteView,
        meta: { title: 'Dashboard', keepAlive: true, icon: bxAnaalyse, permission: [ 'dashboard' ] },
        children: [
          {
            path: 'analysis',
            name: 'Analysis',
            component: () => import('@/views/admin/dashboard/Analysis'),
            meta: { title: 'Analysis', keepAlive: false }
          },
          {
            path: 'workplace',
            name: 'Workplace',
            component: () => import('@/views/admin/dashboard/Workplace'),
            meta: { title: 'Workplace', keepAlive: true }
          }
        ]
      },
      // product
      {
        path: 'product',
        name: 'Product',
        redirect: '/admin/product/productList',
        component: PageView,
        meta: { title: 'Product', keepAlive: true, permission: [ 'product' ] },
        children: [
          {
            path: 'productList',
            name: 'ProductList',
            component: () => import('@/views/admin/product/list'),
            meta: { title: 'Product', keepAlive: false },
          },
          {
            path: 'productEdit/:id(\\d+)',
            name: 'ProductEdit',
            component: () => import('@/views/admin/product/edit'),
            meta: { title: 'Product Edit', keepAlive: false },
            hidden: true
          },
          {
            path: 'productCreate',
            name: 'ProductCreate',
            component: () => import('@/views/admin/product/create'),
            meta: { title: 'Product Create', keepAlive: false },
            hidden: true
          },
        ]
      },
      // product variant
      {
        path: 'variant',
        name: 'Variant',
        redirect: '/admin/variant/variantList',
        component: PageView,
        meta: { title: 'Variant', keepAlive: true, permission: [ 'product' ] },
        children: [
          {
            path: 'variantList',
            name: 'VariantList',
            component: () => import('@/views/admin/variant/list'),
            meta: { title: 'Variant', keepAlive: false },
          },
          {
            path: 'variantEdit/:id(\\d+)',
            name: 'VariantEdit',
            component: () => import('@/views/admin/variant/edit'),
            meta: { title: 'Edit', keepAlive: false },
            hidden: true
          },
          {
            path: 'variantCreate',
            name: 'VariantCreate',
            component: () => import('@/views/admin/variant/create'),
            meta: { title: 'Create', keepAlive: false },
            hidden: true
          },
        ]
      },
      // order
      {
        path: 'order',
        name: 'Order',
        redirect: '/admin/order/orderList',
        component: PageView,
        meta: { title: 'Order', keepAlive: true, permission: [ 'product' ] },
        children: [
          {
            path: 'orderList',
            name: 'OrderList',
            component: () => import('@/views/admin/order/list'),
            meta: { title: 'Order', keepAlive: false },
          },
          {
            path: 'orderEdit/:id(\\d+)',
            name: 'OrderEdit',
            component: () => import('@/views/admin/order/edit'),
            meta: { title: 'Edit', keepAlive: false },
            hidden: true
          },
          {
            path: 'orderCreate',
            name: 'OrderCreate',
            component: () => import('@/views/admin/order/create'),
            meta: { title: 'Create', keepAlive: false },
            hidden: true
          },
        ]
      },
      //Category
      // {
      //   path: 'category',
      //   name: 'Category',
      //   redirect: '/admin/category/categoryList',
      //   component: PageView,
      //   meta: { title: 'Category', keepAlive: true, permission: [ 'product' ] },
      //   children: [
      //     {
      //       path: 'categoryList',
      //       name: 'CategoryList',
      //       component: () => import('@/views/admin/category/list'),
      //       meta: { title: 'Category', keepAlive: false }
      //     }
      //   ]
      // },
      //Source
      {
        path: 'source',
        name: 'Source',
        redirect: '/admin/source/sourceList',
        component: PageView,
        meta: { title: 'Source', keepAlive: true, permission: [ 'product' ] },
        children: [
          {
            path: 'sourceList',
            name: 'SourceList',
            component: () => import('@/views/admin/source/list'),
            meta: { title: 'Source', keepAlive: false }
          }
        ]
      },
      //users
      {
        path: 'user',
        name: 'Users',
        component: PageView,
        meta: { title: 'Users', keepAlive: true, permission: [ 'user' ] },
        redirect: '/admin/user/users',
        children: [
          {
            path: 'users',
            name: 'UserList',
            component: () => import('@/views/admin/user/list'),
            meta: { title: 'Users', keepAlive: true }
          }
        ]
      },
      //roles
      {
        path: 'role',
        name: 'Roles',
        component: PageView,
        meta: { title: 'Roles', keepAlive: true, permission: [ 'role', 'permission' ] },
        redirect: '/admin/role/roles',
        children: [
          {
            path: 'roles',
            name: 'RoleList',
            component: () => import('@/views/admin/role/RoleList'),
            meta: { title: 'Roles', keepAlive: true, permission: [ 'role' ] }
          },
          {
            path: 'permissions',
            name: 'PermissionList',
            component: () => import('@/views/admin/role/PermissionList'),
            meta: { title: 'Permission', keepAlive: true, permission: [ 'permission' ] }
          }
        ]
      },
      // account
      {
        path: 'account',
        name: 'account',
        component: PageView,
        redirect: '/admin/account/center',
        meta: { title: 'Account', keepAlive: true },
        children: [
          {
            path: 'center',
            name: 'center',
            component: () => import('@/views/admin/account/center/Index'),
            meta: { title: 'Account', keepAlive: true }
          },
          {
            path: 'settings',
            name: 'settings',
            component: () => import('@/views/admin/account/settings/Index'),
            meta: { title: 'Profile', hideHeader: true },
            redirect: '/admin/account/settings/base',
            hideChildrenInMenu: true,
            children: [
              {
                path: 'base',
                name: 'BaseSettings',
                component: () => import('@/views/admin/account/settings/BaseSetting'),
                meta: { title: 'Base Settings', hidden: true }
              },
              {
                path: 'security',
                name: 'SecuritySettings',
                component: () => import('@/views/admin/account/settings/Security'),
                meta: { title: 'Security Settings', hidden: true, keepAlive: true }
              },
              {
                path: 'custom',
                name: 'CustomSettings',
                component: () => import('@/views/admin/account/settings/Custom'),
                meta: { title: 'Custom Settings', hidden: true, keepAlive: true }
              },
              {
                path: 'binding',
                name: 'BindingSettings',
                component: () => import('@/views/admin/account/settings/Binding'),
                meta: { title: 'Binding Settings', hidden: true, keepAlive: true }
              },
              {
                path: 'notification',
                name: 'NotificationSettings',
                component: () => import('@/views/admin/account/settings/Notification'),
                meta: { title: 'Notification Settings', hidden: true, keepAlive: true }
              }
            ]
          }
        ]
      },
    ]
  },
  {
    path: '*', redirect: '/404', hidden: true
  }
]

/**
 * 基础路由
 * @type { *[] }
 */
export const constantRouterMap = [
  {
    path: '/',
    name: 'index',
    redirect: '/home',
    component: () => import('@/views/layouts/BasicLayout'),
    children: [
      {
        path: 'home',
        name: 'Home',
        component: () => import('@/views/layouts/PageView'),
        redirect: '/home/ticket',
        meta: { title: '首页', keepAlive: true },
        children: [
          {
            path: 'index',
            name: 'HomePage',
            component: () => import('@/views/home/index'),
            meta: { title: '首页', keepAlive: true },
          },
          {
            path: 'ticket',
            name: 'Ticket',
            component: () => import('@/views/home/ticket'),
            meta: { title: '门票', keepAlive: true },
            
          },
          {
            path: 'ticket/:id(\\d+)',
            name: 'TicketDetail',
            component: () => import('@/views/home/detail'),
            meta: { title: '门票', keepAlive: true },
            hidden: true
          },
          {
            path: 'food',
            name: 'Food',
            component: () => import('@/views/home/food'),
            meta: { title: '美食', keepAlive: true },
          },
          {
            path: 'food/:id(\\d+)',
            name: 'FoodDetail',
            component: () => import('@/views/home/detail'),
            meta: { title: '美食', keepAlive: true },
            hidden: true
          },
          {
            path: 'trip',
            name: 'Trip',
            component: () => import('@/views/home/trip'),
            meta: { title: '日游', keepAlive: true },
          },
          {
            path: 'trip/:id(\\d+)',
            name: 'TripDetail',
            component: () => import('@/views/home/detail'),
            meta: { title: '日游', keepAlive: true },
            hidden: true
          },
          {
            path: 'car',
            name: 'Car',
            component: () => import('@/views/home/car'),
            meta: { title: '用车', keepAlive: true },
          },
          {
            path: 'car/:id(\\d+)',
            name: 'CarDetail',
            component: () => import('@/views/home/detail'),
            meta: { title: '用车', keepAlive: true },
            hidden: true
          },
          {
            path: 'hotel',
            name: 'Hotel',
            component: () => import('@/views/home/hotel'),
            meta: { title: '酒店', keepAlive: true },
          },
          {
            path: 'hotel/:id(\\d+)',
            name: 'HotelDetail',
            component: () => import('@/views/home/detail'),
            meta: { title: '酒店', keepAlive: true },
            hidden: true
          },
          {
            path: 'gift',
            name: 'Gift',
            component: () => import('@/views/home/gift'),
            meta: { title: '伴手礼', keepAlive: true },
          },
          {
            path: 'gift/:id(\\d+)',
            name: 'GiftDetail',
            component: () => import('@/views/home/detail'),
            meta: { title: '伴手礼', keepAlive: true },
            hidden: true
          },
          {
            path: 'checkout',
            name: 'Checkout',
            component: () => import('@/views/home/checkout/checkout'),
            meta: { title: '订单信息', keepAlive: true, hiddenHeaderContent: true },
            hidden: true
          }
        ]
      },
    ]
  },
  {
    path: '/user',
    component: UserLayout,
    redirect: '/user/login',
    hidden: true,
    children: [
      {
        path: 'login',
        name: 'login',
        component: () => import('@/views/admin/user/Login')
      },
    ]
  },
  {
    path: '/admin',
    component: UserLayout,
    hidden: true,
    redirect: '/admin/login',
    children: [
      {
        path: 'login',
        name: 'loginadmin',
        component: () => import('@/views/admin/user/Login')
      }
    ]
  },

  {
    path: '/404',
    component: () => import('@/views/exception/404')
  }
]
