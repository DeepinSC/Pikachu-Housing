import provider from '../../api/houseProvider'

const state = {
  list: [],
  detail: {},
}

const getters = {}

const actions = {
  getList ({ commit }, query) {
    provider.getProviderList(providers => {
      commit('setProviderList', providers)
    }, query)
  },
}

const mutations = {
  setProviderList(state, providers) {
    state.list = providers
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
