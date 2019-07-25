import api from './index'
import { axios } from '@/utils/request'

export function getPriceList (parameter) {
  return axios({
    url: api.price,
    method: 'get',
    params: parameter
  })
}

export function getPrice (pk) {
  return axios({
    url: api.price + `${pk}/`,
    method: 'get',
  })
}

export function updatePrice (pk, data) {
  return axios({
    url: api.price + `${pk}/`,
    method: 'put',
    data: data
  })
}

export function createPrice (data) {
  return axios({
    url: api.price,
    method: 'post',
    data: data
  })
}

export function deletePrice (pk) {
  return axios({
    url: api.price + `${pk}/`,
    method: 'delete',
  })
}
