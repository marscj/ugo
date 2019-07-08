import api from './index'
import { axios } from '@/utils/request'

export function upload (formData) {
  return axios.post(api.source, formData)
}