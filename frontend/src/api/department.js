import provider from '../utils/provider'

export default {
  getDepartmentList (cb) {
    let url = "/api/department/"
    provider.get(url).then(response => {
      setTimeout(() => cb(response.data) , 100)
    })
  }
}
