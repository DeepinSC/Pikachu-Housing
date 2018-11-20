import provider from '../utils/provider'

export default {
  getHouseList (cb, query={}) {
    let url = "/api/house/"
    if (Object.keys(query).length !== 0) {
      // url = `/api/house/?name=${query.name}`
      url = "/api/house/?"
      Object.keys(query).forEach((key) => {
        url += key + "=" + query[key]
      })
    }
    provider.get(url).then(response => {
      setTimeout(() => cb(response.data) , 100)
    })
  },

  deleteHouse (id, cb) {
    const url = `/api/house/${id}/`
    provider.delete(url).then(response => this.getHouseList(cb))
  },

  createHouse (data, cb) {
    const url = "/api/house/"
    provider.post(url, data).then(response => this.getHouseList(cb))
  },

  editHouse (data, id, cb) {
    const url = `/api/house/${id}/`
    provider.patch(url, data).then(response => this.getHouseDetail(id, cb))
  },

  getHouseDetail (id, cb) {
    const url = `/api/house/${id}/`
    provider.get(url).then(response => {
      setTimeout(() => cb(response.data) , 100)
    })
  },
}
