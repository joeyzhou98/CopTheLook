<template>
  <div :style="{background: isDark ? '#424242' : '#EEEEEE'}" style="height: 100%">
    <v-toolbar :dark="isDark">
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>ShopTheLook</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-tooltip bottom>
        <template data-app v-slot:activator="{ on, attrs }">
          <v-btn v-bind="attrs" v-on="on" icon @click="reset">
            <v-icon>mdi-restart</v-icon>
          </v-btn>
        </template>
        <span>Reset search</span>
      </v-tooltip>

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

    <div class="text-center ma-2">
      <v-snackbar
        v-model="snackbar"
        color="red darken-2"
      >
        {{ error }}

        <template v-slot:action="{ attrs }">
          <v-btn
            color="blue"
            text
            v-bind="attrs"
            @click="snackbar = false"
          >
            Close
          </v-btn>
        </template>
      </v-snackbar>
    </div>

    <div>
      <v-row justify="center">
        <v-col cols="12" sm="8">
          <v-card height="100%" v-if="notSearched" :dark="isDark" :loading="loading" elevation="16" class="mx-auto">
            <v-card-title>
              <span class="headline" :class="{'black--text': !isDark, 'white--text': isDark}">What style would you like to explore today?</span>
              <v-spacer></v-spacer>
              <v-tooltip right>
                <template v-slot:activator="{ on, attrs }">
                  <div v-bind="attrs" v-on="on">
                    <v-btn :loading="loading" :color="isDark ? 'grey darken-3' : 'grey lighten-3'" :disabled="submitBtnDisabled" @click="uploadFile"
                      >Search</v-btn
                    >
                  </div>
                </template>
                <span v-if="submitBtnDisabled">Please choose a picture</span>
                <span v-else>Upload picture</span>
              </v-tooltip>
            </v-card-title>
            <div>
              <VueFileAgent
                :disabled="loading"
                v-model="files"
                :multiple="false"
                :editable="true"
                :deletable="true"
                helpText="Drop image here or browse"
                @delete="fileDeleted"
                @select="fileSelected"
              ></VueFileAgent>
            </div>
          </v-card>

          <v-img
            v-else
            contain
            :src="'api/' + mainPicture"
            max-height="600"
          >
          </v-img>

          <v-container>
            <v-row dense>
              <Class
                v-for="segment in segments"
                :key="segment.class"
                :class-name="segment.class"
                :img-name="segment.img_name"
                :urls="segment.urls"
                :color="isDark ? '#b4b4b4' : '#EEEEEE'"
              ></Class>
            </v-row>
          </v-container>
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import VueFileAgent from 'vue-file-agent'
import axios from 'axios'
import Class from '../components/Class'
// eslint-disable-next-line no-unused-vars
import VueFileAgentStyles from 'vue-file-agent/dist/vue-file-agent.css'

Vue.use(VueFileAgent)

export default {
  name: 'home',
  components: { 'Class': Class },
  data () {
    return {
      mainPicture: '',
      segments: [],
      error: '',
      isDark: false,
      files: [],
      submitBtnDisabled: true,
      particlesKey: 0,
      loading: false,
      notSearched: true,
      snackbar: false
    }
  },
  methods: {
    changeTheme () {
      this.isDark = !this.isDark
      // this.particlesKey += 1
    },
    openSource () {
      window.open('https://github.com/joeyzhou98/codejam2020', '_blank')
    },
    initParticles () {
      // window.particlesJS('particles-js', {})
    },
    async uploadFile () {
      this.loading = true
      let formData = new FormData()
      formData.append('file', this.files[0].file)

      await axios
        .post('api/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then((response) => {
          const data = response.data
          this.mainPicture = data.main_img_name
          this.segments = data.segments
          this.notSearched = false
        })
        .catch(function (error) {
          if (error.response) {
            this.error = error.response.data
          } else { this.error = 'uh oh, an error happened...' }
          this.loading = false
          this.snackbar = true
        })
      this.loading = false
    },
    fileDeleted () {
      this.files = []
      this.submitBtnDisabled = true
    },
    fileSelected () {
      this.submitBtnDisabled = false
    },
    reset () {
      this.mainPicture = ''
      this.segments = []
      this.files = []
      this.submitBtnDisabled = true
      this.loading = false
      this.notSearched = true
      this.snackbar = false
    }
  },
  mounted () {
    // this.initParticles()
  }
}
</script>

<style scoped>
#tsparticles {
  height: 100%;
  width: 100%;
  position: absolute;
}
</style>
