<template>
  <v-col cols="12">
    <v-hover v-slot="{ hover }">
      <v-card
        :color="color"
        @click="show = !show && urls.length > 0"
        :elevation="hover ? 12 : 2"
        :class="{ 'on-hover': hover, 'show': show }"
      >
        <div class="d-flex flex-no-wrap justify-space-between">
          <div>
            <v-card-title
                class="headline"
                v-text="className"
            ></v-card-title>

            <v-card-subtitle v-text="'Found ' + urls.length + ' links'"></v-card-subtitle>
          </div>

          <v-avatar
              class="ma-3"
              size="125"
              tile
          >
            <v-img contain :src="'api/' + imgName"></v-img>
          </v-avatar>
        </div>
      </v-card>
    </v-hover>

    <v-expand-transition v-if="urls.length > 0">
        <div v-show="show">
          <v-card-text>
            <v-list dense>
              <v-list-item
                v-for="url in urls"
                :key="url"
              >
                <v-list-item-content>
                  <v-tooltip bottom>
                    <template data-app v-slot:activator="{ on, attrs }">
                      <v-btn
                        tile
                        v-bind="attrs"
                        v-on="on"
                        @click="openLink(url)"
                      >{{ url.replace('https://', '').replace('http://', '').split('/')[0] }}</v-btn>
                    </template>
                    <span>{{ url }}</span>
                  </v-tooltip>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card-text>
        </div>
      </v-expand-transition>
  </v-col>
</template>

<script>
export default {
  name: 'Class',
  props: {
    className: String,
    urls: Array,
    imgName: String,
    color: String
  },
  data: function () {
    return {
      items: [],
      show: false
    }
  },
  methods: {
    openLink: function (url) {
      window.open(url, '_blank')
    }
  }
}
</script>

<style>
.v-card {
  transition: opacity .4s ease-in-out;
}
.v-card:not(.on-hover):not(.show) {
  opacity: 0.8;
 }
</style>
