import api from './index'
import { axios } from '@/utils/request'

export function getUserList (parameter) {
  return axios({
    url: api.user,
    method: 'get',
    params: parameter
  })
}

export function getCompanyUserList (parameter) {
  return axios({
    url: api.companyUser,
    method: 'get',
    params: parameter
  })
}

export function getRoleList (parameter) {
  return axios({
    url: api.role,
    method: 'get',
    params: parameter
  })
}

export function getPermissions (parameter) {
  return axios({
    url: api.permission,
    method: 'get',
    params: parameter
  })
}
