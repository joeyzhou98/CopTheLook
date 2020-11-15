import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import './filters'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false

// const baseURL = 'http://localhost:5000';
// if (typeof baseURL !== 'undefined') {
//   Vue.axios.defaults.baseURL = baseURL;
// }

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
