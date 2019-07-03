import api from './index'
import { axios } from '@/utils/request'

export function getCategoryList (parameter) {
  return axios({
    url: api.category,
    method: 'get',
    params: parameter
  })
}
