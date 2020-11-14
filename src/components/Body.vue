<template>
    <div class="hero-body">
                <div class="container has-text-centered">
                    <div class="column is-6 is-offset-3">
                        <h1 class="title">
                            Search for video
                        </h1>
                        <div class="box">
                            <div class="field is-grouped">
                                <p class="control is-expanded">
                                    <input class="input" type="text" placeholder="Search">
                                </p>
                                <p class="control">
                                    <a href="" @click.prevent="searchYoutubeVideos" class="button is-info">
                                        Submit
                                    </a>
                                </p>
                            </div>
                        </div>
                        <h4>Results</h4>
                <p v-for="r in resources" :key="r">
                  Server Timestamp: {{ r }}
                </p>
                <p>{{error}}</p>
                    </div>
                </div>
            </div>
</template>

<script>
import $backend from '../backend'

export default {
  name: 'Body',
  props: {
  },
  data () {
    return {
      resources: [],
      error: ''
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
    searchYoutubeVideos () {
      $backend.searchYoutubeVideos()
        .then(responseData => {
          this.resources.push(responseData);
        }).catch(error => {
          this.error = error.message
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
