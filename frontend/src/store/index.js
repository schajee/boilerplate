import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    key: 0,
    access: null,
    refresh: null,
    user: null,
    socket: {
      isConnected: false,
      message: '',
      reconnectError: false,
    }
  },
  mutations: {
    login(state, payload) {
      state.access = payload.access
      state.refresh = payload.refresh
      state.user = payload.user
    },
    logout(state) {
      state.access = null
      state.refresh = null
      state.user = null
    },
    refresh(state, payload) {
      state.access = payload
    },
    SOCKET_ONOPEN (state, event)  {
      Vue.prototype.$socket = event.currentTarget
      state.socket.isConnected = true
    },
    SOCKET_ONCLOSE (state)  {
      state.socket.isConnected = false
    },
    SOCKET_ONERROR (state, event)  {
      console.error(state, event)
    },
    // default handler called for all methods
    SOCKET_ONMESSAGE (state, message)  {
      state.socket.message = JSON.parse(message.data)
      state.key += 1
    },
    // mutations for reconnect methods
    SOCKET_RECONNECT(state, count) {
      console.info(state, count)
    },
    SOCKET_RECONNECT_ERROR(state) {
      state.socket.reconnectError = true;
    },
  },
  actions: {
  },
  modules: {
  },
  plugins: [createPersistedState()],
})
