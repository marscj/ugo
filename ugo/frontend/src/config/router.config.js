import { UserLayout, BasicLayout, RouteView, BlankLayout, PageView } from '@/layouts'
import { bxAnaalyse } from '@/core/icons'

export const asyncRouterMap = [
  {
    path: '/',
    name: 'index',
    component: () => import('@/views/home/index'),
    hidden: true
  },
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
            component: () => import('@/views/dashboard/Analysis'),
            meta: { title: 'Analysis', keepAlive: false, permission: [ 'dashboard' ] }
          },
          {
            path: 'workplace',
            name: 'Workplace',
            component: () => import('@/views/dashboard/Workplace'),
            meta: { title: 'Workplace', keepAlive: true, permission: [ 'dashboard' ] }
          }
        ]
      },
      // account
      {
        path: 'account',
        name: 'account',
        component: RouteView,
        redirect: '/admin/account/center',
        meta: { title: 'Account', icon: 'user', keepAlive: true },
        children: [
          {
            path: 'center',
            name: 'center',
            component: () => import('@/views/account/center/Index'),
            meta: { title: 'Account', keepAlive: true }
          },
          {
            path: 'settings',
            name: 'settings',
            component: () => import('@/views/account/settings/Index'),
            meta: { title: 'Profile', hideHeader: true },
            redirect: '/admin/account/settings/base',
            hideChildrenInMenu: true,
            children: [
              {
                path: 'base',
                name: 'BaseSettings',
                component: () => import('@/views/account/settings/BaseSetting'),
                meta: { title: 'Base Settings', hidden: true }
              },
              {
                path: 'security',
                name: 'SecuritySettings',
                component: () => import('@/views/account/settings/Security'),
                meta: { title: 'Security Settings', hidden: true, keepAlive: true }
              },
              {
                path: 'custom',
                name: 'CustomSettings',
                component: () => import('@/views/account/settings/Custom'),
                meta: { title: 'Custom Settings', hidden: true, keepAlive: true }
              },
              {
                path: 'binding',
                name: 'BindingSettings',
                component: () => import('@/views/account/settings/Binding'),
                meta: { title: 'Binding Settings', hidden: true, keepAlive: true }
              },
              {
                path: 'notification',
                name: 'NotificationSettings',
                component: () => import('@/views/account/settings/Notification'),
                meta: { title: 'Notification Settings', hidden: true, keepAlive: true }
              }
            ]
          }
        ]
      },
      {
        path: 'user',
        name: 'Users',
        component: RouteView,
        meta: { title: 'Users', icon: 'user', permission: [ 'user' ] },
        redirect: '/admin/user/users',
        children: [
          {
            path: 'users',
            name: 'UserList',
            component: () => import('@/views/user/UserList'),
            meta: { title: 'Users', keepAlive: true }
          }
        ]
      },
      {
        path: 'role',
        name: 'Roles',
        component: RouteView,
        meta: { title: 'Roles', icon: 'user', permission: [ 'role', 'permission' ] },
        redirect: '/admin/role/roles',
        children: [
          {
            path: 'roles',
            name: 'SystemRole',
            component: () => import('@/views/role/RoleList'),
            meta: { title: 'Roles', keepAlive: true, permission: [ 'role' ] }
          },
          {
            path: 'permissions',
            name: 'PermissionList',
            component: () => import('@/views/role/PermissionList'),
            meta: { title: 'Permission', keepAlive: true, permission: [ 'permission' ] }
          }
        ]
      }
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
    path: '/user',
    component: UserLayout,
    redirect: '/user/login',
    hidden: true,
    children: [
      {
        path: 'login',
        name: 'login',
        component: () => import('@/views/user/Login')
      }
    ]
  },

  {
    path: '/404',
    component: () => import('@/views/exception/404')
  }

]


// import { UserLayout, BasicLayout, RouteView, BlankLayout, PageView } from '@/layouts'
// import { bxAnaalyse } from '@/core/icons'

// export const asyncRouterMap = [

//   {
//     path: '/',
//     name: 'index',
//     component: BasicLayout,
//     meta: { title: 'Dashboard' },
//     redirect: '/dashboard/workplace',
//     children: [
//       // dashboard
//       {
//         path: '/dashboard',
//         name: 'dashboard',
//         redirect: '/dashboard/workplace',
//         component: RouteView,
//         meta: { title: 'Dashboard', keepAlive: true, icon: bxAnaalyse, permission: [ 'dashboard' ] },
//         children: [
//           {
//             path: '/dashboard/analysis',
//             name: 'Analysis',
//             component: () => import('@/views/dashboard/Analysis'),
//             meta: { title: 'Analysis', keepAlive: false, permission: [ 'dashboard' ] }
//           },
//           {
//             path: '/dashboard/workplace',
//             name: 'Workplace',
//             component: () => import('@/views/dashboard/Workplace'),
//             meta: { title: 'Workplace', keepAlive: true, permission: [ 'dashboard' ] }
//           }
//         ]
//       },

//       // account
//       {
//         path: '/account',
//         component: RouteView,
//         redirect: '/account/center',
//         name: 'account',
//         meta: { title: 'Account', icon: 'user', keepAlive: true },
//         children: [
//           {
//             path: '/account/center',
//             name: 'center',
//             component: () => import('@/views/account/center/Index'),
//             meta: { title: 'Account', keepAlive: true }
//           },
//           {
//             path: '/account/settings',
//             name: 'settings',
//             component: () => import('@/views/account/settings/Index'),
//             meta: { title: 'My Settrings', hideHeader: true },
//             redirect: '/account/settings/base',
//             hideChildrenInMenu: true,
//             children: [
//               {
//                 path: '/account/settings/base',
//                 name: 'BaseSettings',
//                 component: () => import('@/views/account/settings/BaseSetting'),
//                 meta: { title: 'Base Settings', hidden: true }
//               },
//               {
//                 path: '/account/settings/security',
//                 name: 'SecuritySettings',
//                 component: () => import('@/views/account/settings/Security'),
//                 meta: { title: 'Security Settings', hidden: true, keepAlive: true }
//               },
//               {
//                 path: '/account/settings/custom',
//                 name: 'CustomSettings',
//                 component: () => import('@/views/account/settings/Custom'),
//                 meta: { title: 'Custom Settings', hidden: true, keepAlive: true }
//               },
//               {
//                 path: '/account/settings/binding',
//                 name: 'BindingSettings',
//                 component: () => import('@/views/account/settings/Binding'),
//                 meta: { title: 'Binding Settings', hidden: true, keepAlive: true }
//               },
//               {
//                 path: '/account/settings/notification',
//                 name: 'NotificationSettings',
//                 component: () => import('@/views/account/settings/Notification'),
//                 meta: { title: 'Notification Settings', hidden: true, keepAlive: true }
//               }
//             ]
//           }
//         ]
//       },
//       {
//         path: '/user',
//         name: 'Users',
//         component: RouteView,
//         meta: { title: 'Users', icon: 'user', permission: [ 'user' ] },
//         redirect: '/user/users',
//         children: [
//           {
//             path: '/user/users',
//             name: 'UserList',
//             component: () => import('@/views/user/UserList'),
//             meta: { title: 'Users', keepAlive: true }
//           }
//         ]
//       },
//       {
//         path: '/role',
//         name: 'Roles',
//         component: RouteView,
//         meta: { title: 'Roles', icon: 'user', permission: [ 'role', 'permission' ] },
//         redirect: '/role/roles',
//         children: [
//           {
//             path: '/role/roles',
//             name: 'SystemRole',
//             component: () => import('@/views/role/RoleList'),
//             meta: { title: 'Roles', keepAlive: true, permission: [ 'role' ] }
//           },
//           {
//             path: '/role/permissions',
//             name: 'PermissionList',
//             component: () => import('@/views/role/PermissionList'),
//             meta: { title: 'Permission', keepAlive: true, permission: [ 'permission' ] }
//           }
//         ]
//       }
//     ]
//   },
//   {
//     path: '*', redirect: '/404', hidden: true
//   }
// ]

// /**
//  * 基础路由
//  * @type { *[] }
//  */
// export const constantRouterMap = [
//   {
//     path: '/user',
//     component: UserLayout,
//     redirect: '/user/login',
//     hidden: true,
//     children: [
//       {
//         path: 'login',
//         name: 'login',
//         component: () => import('@/views/user/Login')
//       }
//     ]
//   },

//   {
//     path: '/404',
//     component: () => import('@/views/exception/404')
//   }

// ]
