import api from './index'
import {
  axios
} from '@/utils/request'

export function getBookingList(parameter) {
  return axios({
    url: api.booking,
    method: 'get',
    params: parameter
  })
}

export function getBooking(pk) {
  return axios({
    url: api.booking + `${pk}/`,
    method: 'get',
  })
}

export function updateBooking(pk, data) {
  return axios({
    url: api.booking + `${pk}/`,
    method: 'put',
    data: data
  })
}

export function createBooking(data) {
  return axios({
    url: api.booking,
    method: 'post',
    data: data
  })
}

export function deleteBooking(pk) {
  return axios({
    url: api.booking + `${pk}/`,
    method: 'delete',
  })
}