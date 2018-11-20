import Vue from 'vue'
import Vuex from 'vuex'
import house from './modules/house'
import user from './modules/user'
import provider from './modules/provider'
import department from './modules/department'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    house,
    user,
    provider,
    department,
  },
})
