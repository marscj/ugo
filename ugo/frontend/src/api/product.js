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
