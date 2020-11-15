<template>
  <div :style="{background: isDark ? '#424242' : '#EEEEEE'}" style="height: 100%">
    <v-toolbar :dark="isDark">
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>ShopTheLook</v-toolbar-title>

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
        <v-col cols="12" sm="8">
          <v-card :dark="isDark" :loading="loading" elevation="16" max-width="800" class="mx-auto">
            <v-card-title>
              <span class="headline" :class="{'black--text': !isDark, 'white--text': isDark}">What kind of style would you like to explore today?</span>
              <v-spacer></v-spacer>
              <v-tooltip right>
                <template v-slot:activator="{ on, attrs }">
                  <div v-bind="attrs" v-on="on">
                    <v-btn :loading="loading" :color="isDark ? 'grey darken-3' : 'grey lighten-3'" :disabled="submitBtnDisabled" @click="uploadFile"
                      >Upload</v-btn
                    >
                  </div>
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

          <v-container>
            <v-row dense>
              <Class
                v-for="segment in segments"
                :key="segment.class"
                :class-name="segment.class"
                :img-name="segment.img_name"
                :urls="segment.urls"
                :color="'#'+(Math.random()*0xFFFFFF<<0).toString(16)"
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
      isDark: true,
      files: [],
      submitBtnDisabled: true,
      particlesKey: 0,
      loading: false
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
        })
        .catch(function (error) {
          this.error = error.message
        })
      this.loading = false
    },
    fileDeleted () {
      this.files = []
      this.submitBtnDisabled = true
    },
    fileSelected () {
      this.submitBtnDisabled = false
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
