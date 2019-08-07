export function  checkError(error, ...fields) {
  if(error && error.response && error.response.data && error.response.data.message) {
    var data = {}
    for(var field of fields) {
      data[field] = error.response.data.message[field] || null
    }
    return data
  }
  return null
}