<template>
  <v-app>
    <v-main>
      <v-toolbar dark max-height="60" min-height="60">
        <v-toolbar-title>Pixiv Ranking Viewer</v-toolbar-title>
        <v-spacer></v-spacer>
        <tweet v-bind:pics="pics" v-bind:slideItemNo="slideItemNo"></tweet>
        <SelectRankingGenre></SelectRankingGenre>
      </v-toolbar>
      <router-view
        v-on:pics="getPics"
        v-on:slideItemNo="getSlideNo"
      ></router-view>
    </v-main>
  </v-app>
</template>

<script>
import SelectRankingGenre from "@/components/modal/SelectRankingGenre";
import tweet from "@/components/modal/tweet";

export default {
  name: "App",
  components: {
    SelectRankingGenre,
    tweet
  },
  data() {
    return {
      pics: [],
      slideItemNo: 0
    };
  },
  methods: {
    getPics(vals) {
      // 子コンポーネントからpicsを受け取って格納
      this.pics = vals;
    },
    getSlideNo(slideNo) {
      this.slideItemNo = slideNo;
    }
  }
};
</script>
