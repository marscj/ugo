import api from './index'
import { axios } from '@/utils/request'

export function getCouponList (parameter) {
  return axios({
    url: api.coupon,
    method: 'get',
    params: parameter
  })
}

export function getCoupon (pk) {
  return axios({
    url: api.coupon + `${pk}/`,
    method: 'get',
  })
}

export function updateCoupon (pk, data) {
  return axios({
    url: api.coupon + `${pk}/`,
    method: 'put',
    data: data
  })
}

export function createCoupon (data) {
  return axios({
    url: api.coupon,
    method: 'post',
    data: data
  })
}

export function deleteCoupon (pk) {
  return axios({
    url: api.coupon + `${pk}/`,
    method: 'delete',
  })
}