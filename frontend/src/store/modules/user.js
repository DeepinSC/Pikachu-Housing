import user from '../../api/user'

const state = {
  detail: {
    username: "Anonymous User",
    id: -1,
  },
  next: "",
  status: false,
}

const getters = {}

const actions = {
  getUser({commit}) {
    user.getUser(user => {
      commit('setUserDetail', user)
    })
  },
  logout({commit}) {
    user.logout((data) => {
      commit('resetUser',data.next)
    })
  },
  login({ commit }, data) {
    user.login(data, user => {
      commit('setUserDetail', user)
    }, e => {state.status = false})
  },
  signup({commit}, data) {
    user.signup(data, () => {
      commit('setStatusFailure')
    },data)
  },
}

const mutations = {
  setUserDetail(state, user) {
    state.detail = user
    state.status = true
  },
  resetUser(state, next) {
    state.detail = {username: "Anonymous User", id: -1}
    state.next = next
  },
  setStatusFailure(state, user) {
    state.status = false
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
