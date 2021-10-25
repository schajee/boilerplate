import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

Vue.config.productionTip = false

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.baseURL = `http://${process.env.VUE_APP_SERVER}/api`

// Inject authorization headers
axios.interceptors.request.use(
  (config) => {
    let token = store.state.access
    if (token) config.headers['Authorization'] = `Bearer ${token}`
    return config
  }, (error) => { return Promise.reject(error) }
)

// Refresh token if possible, else route to login
import createAuthRefreshInterceptor from 'axios-auth-refresh';
// Function that will be called to refresh authorization
const refreshAuthLogic = failedRequest => axios.post('/token/refresh/', { refresh: store.state.refresh }).then(tokenRefreshResponse => {
    store.commit('refresh', tokenRefreshResponse.data.access)
    failedRequest.response.config.headers['Authorization'] = `Bearer ${tokenRefreshResponse.data.access}`
    return Promise.resolve()
}).catch(() => router.push('/login'))
// Instantiate the interceptor
createAuthRefreshInterceptor(axios, refreshAuthLogic, { statusCodes: [ 401, 403 ]});

// Connect websocket
import VueNativeSock from 'vue-native-websocket'
if (store.state.user) {
  Vue.use(VueNativeSock, `ws://${process.env.VUE_APP_SERVER}/notify/${store.state.user.username}/`, {
    reconnection: true,
    // reconnectionAttempts: 0,
    // reconnectionDelay: 5000,
    store: store
  })
}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
