import api from './index'
import { axios } from '@/utils/request'

export function getProductList (parameter) {
  return axios({
    url: api.product + '?backend=0' ,
    method: 'get',
    params: parameter
  })
}

export function getProduct (pk) {
  return axios({
    url: api.product + `${pk}/` + '?backend=0',
    method: 'get',
  })
}

export function updateProduct (pk, data) {
  return axios({
    url: api.product + `${pk}/` + '?backend=0',
    method: 'put',
    data: data
  })
}

export function createProduct (data) {
  return axios({
    url: api.product + '?backend=0',
    method: 'post',
    data: data
  })
}

export function deleteProduct (pk) {
  return axios({
    url: api.product + `${pk}/` + '?backend=0',
    method: 'delete',
  })
}

export function listProductDelete (parameter) {
  return axios({
    url: api.product + 'delete/',
    method: 'delete',
    params: parameter
  })
}

export function listProductEnable (parameter) {
  return axios({
    url: api.product + 'enable/',
    method: 'post',
    params: parameter
  })
}

export function getVariantList (parameter) {
    return axios({
      url: api.variant + '?backend=0',
      method: 'get',
      params: parameter
    })
  }
  
  export function getVariant (pk) {
    return axios({
      url: api.variant + `${pk}/` + '?backend=0',
      method: 'get',
    })
  }
  
  export function updateVariant (pk, data) {
    return axios({
      url: api.variant + `${pk}/` + '?backend=0',
      method: 'put',
      data: data
    })
  }
  
  export function createVariant (data) {
    return axios({
      url: api.variant + '?backend=0',
      method: 'post',
      data: data
    })
  }
  
  export function deleteVariant (pk) {
    return axios({
      url: api.variant + `${pk}/` + '?backend=0',
      method: 'delete',
    })
  }
  
  export function listVariantDelete (parameter) {
    return axios({
      url: api.variant + 'delete/' ,
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