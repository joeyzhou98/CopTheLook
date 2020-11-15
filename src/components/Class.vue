<template>
  <v-col cols="12">
    <v-card
      :color="color"
    >
      <div class="d-flex flex-no-wrap justify-space-between">
        <div>
          <v-card-title
              class="headline"
              v-text="this.className"
          ></v-card-title>

          <v-card-subtitle v-text="'Found ' + this.urls.length + ' links'"></v-card-subtitle>

          <v-card-actions>
            <v-btn
              @click="show = !show"
              v-if="this.urls.length > 0"
              class="ml-2 mt-5"
              outlined
              rounded
              small
            >
              See links
            </v-btn>
          </v-card-actions>
        </div>

        <v-avatar
            class="ma-3"
            size="125"
            tile
        >
          <v-img :src="'api/' + this.imgName"></v-img>
        </v-avatar>

      </div>

    </v-card>
    <v-expand-transition v-if="this.urls.length > 0">
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
