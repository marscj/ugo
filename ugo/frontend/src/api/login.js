import api from './index'
import { axios } from '@/utils/request'

export function login (parameter) {
  return axios({
    url: api.login,
    method: 'post',
    data: parameter
  })
}

export function getInfo () {
  return axios({
    url: api.userInfo,
    method: 'get',
    headers: {
      'Content-Type': 'application/json;charset=UTF-8'
    }
  })
}

export function logout () {
  return axios({
    url: api.logout,
    method: 'post',
    headers: {
      'Content-Type': 'application/json;charset=UTF-8'
    }
  })
}
