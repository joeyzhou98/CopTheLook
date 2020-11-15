import axios from 'axios'

let $axios = axios.create({
  baseURL: 'http://localhost:5000/api/',
  timeout: 5000,
  headers: { 'Content-Type': 'application/json' }
})

// Request Interceptor
$axios.interceptors.request.use(function (config) {
  config.headers['Authorization'] = 'Fake Token'
  return config
})

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // Handle Error
  console.log(error)
  return Promise.reject(error)
})

export default {

  fetchResource () {
    return $axios.get(`resource/xxx`)
      .then(response => response.data)
  },

  fetchSecureResource () {
    return $axios.get(`secure-resource/zzz`)
      .then(response => response.data)
  },

  reverseImage (path) {
    return $axios.get(`/reverse-image/` + path)
      .then(response => response.data)
  },

  reverseUri (url) {
    return $axios.get(`/reverse-uri/` + url)
      .then(response => response.data)
  }
}
