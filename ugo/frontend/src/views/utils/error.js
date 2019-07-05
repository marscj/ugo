export function  checkError(error, ...fields) {
  if(error && error.response && error.response.data && error.response.data.message) {
    var data = {}
    for(var field of fields) {
      data[field] = error.response.data.message[field] || null
    }
    console.log(data)
    return data
  }
  return null
}