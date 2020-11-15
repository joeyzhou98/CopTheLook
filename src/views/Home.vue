<template>
  <div style="height: 100%;">
    <v-toolbar :dark="isDark">
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Title</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-tooltip bottom>
        <template data-app v-slot:activator="{ on, attrs }">
          <v-btn v-bind="attrs" v-on="on" icon @click="changeTheme">
            <v-icon>mdi-invert-colors</v-icon>
          </v-btn>
        </template>
        <span>Change theme</span>
      </v-tooltip>

      <v-tooltip bottom>
        <template data-app v-slot:activator="{ on, attrs }">
          <v-btn v-bind="attrs" v-on="on" icon @click="openSource">
            <v-icon>mdi-github</v-icon>
          </v-btn>
        </template>
        <span>View source</span>
      </v-tooltip>
    </v-toolbar>
      <div>
        <v-row justify="center">
          <v-col
            cols="12"
            sm="8"
          >
            <v-card max-width="800" class="mx-auto">
              <v-card-title class="blue darken-1">
                <span class="headline white--text">Fashion Shopping Helper</span>
                <v-spacer></v-spacer>
                <v-tooltip right>
                  <template v-slot:activator="{ on, attrs }">
                    <div v-bind="attrs" v-on="on"><v-btn :disabled="submitBtnDisabled" @click="uploadFile">Upload</v-btn></div>
                  </template>
                  <span v-if="submitBtnDisabled">Please choose a picture</span>
                  <span v-else>Upload picture</span>
                </v-tooltip>
              </v-card-title>
              <div>
                <VueFileAgent
                  v-model="files"
                  :multiple="false"
                  :deletable="true"
                  helpText="Drop image here or browse"
                  @delete="fileDeleted"
                  @select="fileSelected"
                ></VueFileAgent>
              </div>
            </v-card>

            <div class="about">
    <h1>Backend Resources Demo</h1>
    <p>Click on the links below to fetch data from the Flask server</p>
    <a href="" @click.prevent="fetchResource">Fetch</a><br/>
    <a href="" @click.prevent="fetchSecureResource">Fetch Secure Resource</a>
    <h4>Results</h4>
    <p v-for="r in resources" :key="r.timestamp">
      Server Timestamp: {{r.timestamp | formatTimestamp }}
    </p>
    <p>{{error}}</p>
  </div>
          </v-col>
        </v-row>
      </div>
  </div>
</template>

<script>
import Vue from 'vue'
import VueFileAgent from 'vue-file-agent'
import axios from 'axios'
// eslint-disable-next-line no-unused-vars
import VueFileAgentStyles from 'vue-file-agent/dist/vue-file-agent.css'
import $backend from '../backend'

Vue.use(VueFileAgent)

export default {
  name: 'home',
  components: {
  },
  data () {
    return {
      resources: [],
      error: '',
      isDark: true,
      files: [],
      submitBtnDisabled: true,
      particlesKey: 0,
      fileName: ''
    }
  },
  methods: {
    fetchResource () {
      $backend.fetchResource()
        .then(responseData => {
          this.resources.push(responseData)
        }).catch(error => {
          this.error = error.message
        })
    },
    fetchSecureResource () {
      $backend.fetchSecureResource()
        .then(responseData => {
          this.resources.push(responseData)
        }).catch(error => {
          this.error = error.message
        })
    },
    changeTheme () {
      // this.isDark = !this.isDark
      // this.particlesKey += 1
    },
    openSource () {
      window.open('https://github.com/joeyzhou98/codejam2020', '_blank')
    },
    initParticles () {
      // window.particlesJS('particles-js', {})
    },
    uploadFile () {
      let formData = new FormData()
      formData.append('file', this.files[0].file)

      axios.post('api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      ).then(function (response) {
        $backend.reverseImage(response.data)
          .then(responseData => {
            this.resources.push(responseData)
            console.log(responseData)
          }).catch(error => {
            this.error = error.message
          })
      }).catch(function (error) {
        console.log(error)
      })
    },
    fileDeleted () {
      this.files = []
      this.submitBtnDisabled = true
    },
    fileSelected () {
      this.submitBtnDisabled = false
    },
    reverseImage (path) {
      $backend.reverseImage(path)
        .then(responseData => {
          this.resources.push(responseData)
          console.log(this.resources)
        }).catch(error => {
          this.error = error.message
        })
    },
    reverseUri (url) {
      $backend.reverseUri(url)
        .then(responseData => {
          this.resources.push(responseData)
          console.log(this.resources)
        }).catch(error => {
          this.error = error.message
        })
    }
  },
  mounted () {
    // this.initParticles()
  }
}
</script>

<style>
#tsparticles {
  height: 100%;
  width: 100%;
  position: absolute;
}
</style>
