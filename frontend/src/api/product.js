import api from './index'
import { axios } from '@/utils/request'

export function getProductList (parameter) {
  return axios({
    url: api.system_product,
    method: 'get',
    params: parameter
  })
}

export function getProduct (pk) {
  return axios({
    url: api.system_product + `${pk}/`,
    method: 'get',
  })
}

export function updateProduct (pk, data) {
  return axios({
    url: api.system_product + `${pk}/`,
    method: 'put',
    data: data
  })
}

export function createProduct (data) {
  return axios({
    url: api.system_product,
    method: 'post',
    data: data
  })
}

export function deleteProduct (pk) {
  return axios({
    url: api.system_product + `${pk}/`,
    method: 'delete',
  })
}

export function getFrontProductList (parameter) {
  return axios({
    url: api.product,
    method: 'get',
    params: parameter
  })
}

export function getFrontProduct (pk) {
  return axios({
    url: api.product + `${pk}/`,
    method: 'get',
  })
}
