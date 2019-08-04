import api from './index'
import { axios } from '@/utils/request'

export function getUserList (parameter) {
  return axios({
    url: api.user,
    method: 'get',
    params: parameter
  })
}

export function updateUser (pk, data) {
  return axios({
    url: api.user + `${pk}/`,
    method: 'put',
    data: data
  })
}

export function getRoleList (parameter) {
  return axios({
    url: api.role,
    method: 'get',
    params: parameter
  })
}

export function createRole (pk, data) {
  return axios({
    url: api.role + `${pk}/`,
    method: 'post',
    data: data
  })
}

export function updateRole (pk, data) {
  return axios({
    url: api.role + `${pk}/`,
    method: 'put',
    data: data
  })
}

export function getPermissions (parameter) {
  return axios({
    url: api.permission,
    method: 'get',
    params: parameter
  })
}
