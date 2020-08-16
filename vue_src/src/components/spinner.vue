<template>
  <div
    class="text-center"
    v-show="loading"
    :elevation="15"
    style="height: auto; width:auto ;"
  >
    <v-overlay>
      <v-progress-circular
        :size="50"
        color="primary"
        indeterminate
      ></v-progress-circular>
    </v-overlay>
  </div>
</template>

<script>
export default {
  name: "App",
  computed: {
    // TODO Vuexを使わずに親子での受け渡しとする
    loading() {
      return this.$store.state.loading;
    }
  }
};
</script>
