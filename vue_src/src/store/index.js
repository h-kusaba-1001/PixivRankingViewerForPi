import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    loading: false
  },
  mutations: {
    set_loading(state) {
      state.loading = !state.loading;
    }
  },
  actions: {},
  modules: {}
});
