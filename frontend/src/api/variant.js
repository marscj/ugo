import api from './index'
import { axios } from '@/utils/request'

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

export function listVariantDelete (parameter) {
  return axios({
    url: api.variant + 'delete/',
    method: 'delete',
    params: parameter
  })
}

export function listVariantEnable (parameter) {
  return axios({
    url: api.variant + 'enable/',
    method: 'post',
    params: parameter
  })
}