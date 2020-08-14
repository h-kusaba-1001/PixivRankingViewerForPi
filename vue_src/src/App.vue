<template>
  <v-app>
    <v-main>
      <toolbar></toolbar>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import toolbar from "./components/toolbar";

export default {
  name: "App",
  components: {
    toolbar
  },
  data: () => ({
    items: [],
  })
};
</script>
