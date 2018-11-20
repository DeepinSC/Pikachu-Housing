import provider from '../utils/provider'

export default {
  getUser (cb) {
    let url = '/api/user/profile'
    provider.get(url).then(response => {
      setTimeout(() => cb(response.data) , 100)
    })
  },
  logout (cb) {
    let url = '/api/user/logout'
    provider.get(url).then(response => {
      setTimeout(() => cb(response.data) , 100)
    })
  },
  login (data, cb, errorcb) {
    const url = "/api/user/signin/"
    provider.post(url, data).then(response => this.getUser(cb)).catch((e) => errorcb(e))
  },
  signup (data, cb, errorcb) {
    const url = "/api/user/signup/"
    provider.post(url, data).then(response => {
      setTimeout(() => cb(response.data), 100)
    })
  },
}
