import api from './index'
import { axios } from '@/utils/request'

export function getProductList (parameter) {
  return axios({
    url: api.product,
    method: 'get',
    params: parameter
  })
}

export function getProduct (pk) {
  return axios({
    url: api.product + `${pk}/`,
    method: 'get',
  })
}

export function updateProduct (pk, data) {
  return axios({
    url: api.product + `${pk}/`,
    method: 'put',
    data: data
  })
}

export function createProduct (data) {
  return axios({
    url: api.product,
    method: 'post',
    data: data
  })
}

export function deleteProduct (pk) {
  return axios({
    url: api.product + `${pk}/`,
    method: 'delete',
  })
}

export function listProductDelete (parameter) {
  return axios({
    url: api.product + 'delete/',
    method: 'delete',
    params: parameter
  })
}

export function listProductEnable (parameter) {
  return axios({
    url: api.product + 'enable/',
    method: 'post',
    params: parameter
  })
}