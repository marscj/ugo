import api from './index'
import { axios } from '@/utils/request'

export function getNoticeList (parameter) {
  return axios({
    url: api.notice,
    method: 'get',
    params: parameter
  })
}

export function getNotice (pk) {
  return axios({
    url: api.notice + `${pk}/`,
    method: 'get',
  })
}

export function updateNotice (pk, data) {
  return axios({
    url: api.notice + `${pk}/`,
    method: 'put',
    data: data
  })
}

export function createNotice (data) {
  return axios({
    url: api.notice,
    method: 'post',
    data: data
  })
}

export function deleteNotice (pk) {
  return axios({
    url: api.notice + `${pk}/`,
    method: 'delete',
  })
}