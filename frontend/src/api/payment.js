import api from './index'
import {
  axios
} from '@/utils/request'

export function paymentRefund(pk) {
  return axios({
    url: api.payment + `${pk}/` + 'refund/',
    method: 'put',
  })
}