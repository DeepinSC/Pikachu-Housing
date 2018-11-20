import provider from '../utils/provider'

export default {
  getProviderList (cb) {
    let url = "/api/provider/"
    provider.get(url).then(response => {
      setTimeout(() => cb(response.data) , 100)
    })
  }
}
