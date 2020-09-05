<template>
  <!-- TODO:サイズの定数化 -->
  <v-carousel
    :cycle="true"
    :interval="30000"
    :progress="true"
    :show-arrows="false"
    :hide-delimiters="true"
    :change="slideItemChanged()"
    height="960"
    v-model="slideNo"
  >
    <v-carousel-item
      v-for="(pic, i) in originPics"
      :key="i"
      :src="pic"
    ></v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
  name: "Main",
  props: {
    pics: Array
  },
  created() {
    this.getPicsApi();
  },
  data() {
    return {
      originPics: [],
      slideNo: 0
    };
  },
  methods: {
    async getPicsApi() {
      let items = [];
      await this.axios
        .get("http://127.0.0.1:8000/get_filepaths")
        .then(response => {
          items = response.data.filepaths;
        })
        .catch(err => console.log("axiosGetErr", err));
      this.originPics = items;
      this.$emit("pics", items);
    },
    slideItemChanged() {
      this.$emit("slideItemNo", this.slideNo);
    }
  }
};
</script>

<style>
.v-image {
  /* dark指定しても背景が白いので、darkを指定 */
  background-color: #272727 !important;
}
.v-image__image--cover {
  /* 縦画面向けの対応 */
  background-size: 100% auto !important;
}
::-webkit-scrollbar {
      display: none;
   }
</style>
