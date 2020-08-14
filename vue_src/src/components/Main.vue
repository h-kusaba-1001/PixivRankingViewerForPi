<template>
  <v-carousel
  :interval="30000"
  :hide-delimiters="true"
  :show-arrows="false"
  height="550"
  >
    <v-carousel-item
      v-for="(item,i) in items"
      :key="i"
      :src="item"
    ></v-carousel-item>
  </v-carousel>
</template>

<script>
  export default {
    data() {
      return {
        items: []
      }
    },
    methods: {
      async getPics() {
        let items = []
        await this.axios.get('http://127.0.0.1:8000/get_filepaths')
        .then(response => {
          items = response.data.filepaths
        })
        .catch(err=>(
          console.log("axiosGetErr",err)
        ))
        this.items = items
      }
    },
    created() {
      this.getPics();
    },
  }
</script>

<style>
  .v-image {
    /* dark指定しても背景が白いので、darkを指定 */
    background-color: #272727 !important
  }
  .v-image__image--cover {
    background-size: auto 100% !important
  }
</style>