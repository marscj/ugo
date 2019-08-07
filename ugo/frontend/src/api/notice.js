import api from './index'
import { axios } from '@/utils/request'

export function getNoticeList (parameter) {
  return axios({
    url: api.system_notice,
    method: 'get',
    params: parameter
  })
}

export function getNotice (pk) {
  return axios({
    url: api.system_notice + `${pk}/`,
    method: 'get',
  })
}

export function updateNotice (pk, data) {
  return axios({
    url: api.system_notice + `${pk}/`,
    method: 'put',
    data: data
  })
}

export function createNotice (data) {
  return axios({
    url: api.system_notice,
    method: 'post',
    data: data
  })
}

export function deleteNotice (pk) {
  return axios({
    url: api.system_notice + `${pk}/`,
    method: 'delete',
  })
}

export function getFrontNoticeList (parameter) {
  return axios({
    url: api.notice,
    method: 'get',
    params: parameter
  })
}

export function getFrontNotice (pk) {
  return axios({
    url: api.notice + `${pk}/`,
    method: 'get',
  })
}