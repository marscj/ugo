import api from './index'
import { axios } from '@/utils/request'

export function getVariantList (parameter) {
  return axios({
    url: api.system_variant,
    method: 'get',
    params: parameter
  })
}

export function getVariant (pk) {
  return axios({
    url: api.system_variant + `${pk}/`,
    method: 'get',
  })
}

export function updateVariant (pk, data) {
  return axios({
    url: api.system_variant + `${pk}/`,
    method: 'put',
    data: data
  })
}

export function createVariant (data) {
  return axios({
    url: api.system_variant,
    method: 'post',
    data: data
  })
}

export function deleteVariant (pk) {
  return axios({
    url: api.system_variant + `${pk}/`,
    method: 'delete',
  })
}

export function getFrontVariantList (parameter) {
  return axios({
    url: api.variant,
    method: 'get',
    params: parameter
  })
}

export function getFrontVariant (pk) {
  return axios({
    url: api.variant + `${pk}/`,
    method: 'get',
  })
}