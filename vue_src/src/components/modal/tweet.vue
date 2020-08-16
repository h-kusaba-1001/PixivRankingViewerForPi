<template>
  <v-dialog v-model="tweetDialog" scrollable max-width="500px">
    <template v-slot:activator="{ on, attrs }">
      <v-btn icon v-bind="attrs" v-on="on">
        <v-icon @click.stop="TweetDialogOpen()">mdi-twitter</v-icon>
      </v-btn>
    </template>
    <v-card>
      <v-toolbar>
        <v-toolbar-title>Tweet</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items>
          <v-btn icon @click="tweetDialog = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-toolbar-items>
      </v-toolbar>
      <v-divider></v-divider>
      <spinner></spinner>
      <v-card-text>
        <v-textarea v-model="tweetDraft"> </v-textarea>
      </v-card-text>
      <v-divider></v-divider>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue" primary text @click="submitBtnClicked()"
          >Tweet!</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import spinner from "../spinner.vue";

export default {
  props: {
    pics: Array,
    slideItemNo: Number
  },
  components: {
    spinner
  },
  data() {
    return {
      gottenPics: this.pics,
      rankingGenre: "",
      tweetDialog: false,
      tweetDraft: ""
    };
  },
  methods: {
    async TweetDialogOpen() {
      // 画像のパスを取得する
      let imgPath = this.$props.pics[this.$props.slideItemNo];
      let imgFileName = imgPath
        .replace("../pixiv_img/", "")
        .replace(".jpg", "")
        .split("_");
      // pixivの作品IDを取得
      let articleId = imgFileName[1];

      await this.axios
        .get("http://127.0.0.1:8000/get_pixiv_info?illust_id=" + articleId)
        .then(response => {
          // console.log(response.data.illust_info)
          this.tweetDraft = response.data.illust_info;
        })
        .catch(err => console.log("axiosGetErr", err));

      // ダイアログオープン
      this.tweetDialog = true;
    },
    async submitBtnClicked() {
      // ローディングをセット
      this.$store.commit("set_loading");
      await this.axios
        .post(
          "http://127.0.0.1:8000/tweet",
          {
            tweet: this.tweetDraft
          },
          {
            headers: {
              "Content-Type": "application/x-www-form-urlencoded"
            }
          }
        )
        .then(() => {})
        .catch(err => {
          alert("通信エラーが発生しました。");
          console.log("Error Occurred!", err);
        });
      // ローディングを解除
      this.$store.commit("set_loading");
      // モーダルを閉じる
      this.tweetDialog = false;
    }
  }
};
</script>
