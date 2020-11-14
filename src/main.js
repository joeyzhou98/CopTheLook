import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import './filters'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

// import Header from '@/components/Header.vue';
// import Body from '@/components/Body.vue';

// Vue.component('app-header', Header);
// Vue.component('app-body', Body);
