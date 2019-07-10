import api from './index'
import { axios } from '@/utils/request'

export function getCategoryList (parameter) {
  return axios({
    url: api.category,
    method: 'get',
    params: parameter
  })
}

export function updateCategory (pk, data) {
  return axios({
    url: api.category + `${pk}/`,
    method: 'put',
    data: data
  })
}

export function createCategory (data) {
  return axios({
    url: api.category,
    method: 'post',
    data: data
  })
}

export function deleteCategory (pk) {
  return axios({
    url: api.category + `${pk}/`,
    method: 'delete',
  })
}

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

export function getVariantList (parameter) {
  return axios({
    url: api.variant,
    method: 'get',
    params: parameter
  })
}

export function getVariant (pk) {
  return axios({
    url: api.variant + `${pk}/`,
    method: 'get',
  })
}

export function updateVariant (pk, data) {
  return axios({
    url: api.variant + `${pk}/`,
    method: 'put',
    data: data
  })
}

export function createVariant (data) {
  return axios({
    url: api.variant,
    method: 'post',
    data: data
  })
}

export function deleteVariant (pk) {
  return axios({
    url: api.variant + `${pk}/`,
    method: 'delete',
  })
}