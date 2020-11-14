<template>
  <v-card
    color="grey lighten-4"
    flat
    height="200px"
    tile
  >
    <v-toolbar dark>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Title</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-invert-colors</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-github</v-icon>
      </v-btn>

    </v-toolbar>
  </v-card>
</template>

<script>
export default {
  name: 'Main'
}
</script>
