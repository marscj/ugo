import api from './index'
import { axios } from '@/utils/request'

export function getCategoryList (parameter) {
  return axios({
    url: api.category,
    method: 'get',
    params: parameter
  })
}

export function updateCategory (data) {
  return axios({
    url: api.category,
    method: 'get',
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
