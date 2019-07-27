import api from './index'
import { axios } from '@/utils/request'

export function getOrderList (parameter) {
  return axios({
    url: api.order,
    method: 'get',
    params: parameter
  })
}

export function getOrder (pk) {
  return axios({
    url: api.order + `${pk}/`,
    method: 'get',
  })
}

export function updateOrder (pk, data) {
  return axios({
    url: api.order + `${pk}/`,
    method: 'put',
    data: data
  })
}

export function createOrder (data) {
  return axios({
    url: api.order,
    method: 'post',
    data: data
  })
}

export function deleteOrder (pk) {
  return axios({
    url: api.order + `${pk}/`,
    method: 'delete',
  })
}
