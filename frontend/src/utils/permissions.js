export function actionToObject (json) {
  try {
    var _json = JSON.stringify(json)
    return JSON.parse(json)
  } catch (e) {
    console.log('err', e.message)
  }
  return []
}
