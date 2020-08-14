<template>
  <v-dialog v-model="rankingGenreDialog" scrollable max-width="500px">
    <template v-slot:activator="{ on, attrs }">
      <v-btn
      icon
      v-bind="attrs"
      v-on="on">
        <v-icon @click.stop="rankingGenreDialog = true">mdi-download</v-icon>
      </v-btn>
    </template>
    <v-card>
      <v-toolbar>
        <v-toolbar-title>ランキングのジャンルを選択してください。</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items>
          <v-btn icon @click="rankingGenreDialog = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-toolbar-items>
      </v-toolbar>
      <v-divider></v-divider>
      <spinner></spinner>
      <v-card-text style="height: 300px;">
        <v-radio-group v-model="rankingGenre" column>
          <v-radio label="日間" value="daily"></v-radio>
          <v-radio label="週間" value="weekly"></v-radio>
          <v-radio label="月間" value="monthly"></v-radio>
          <v-radio label="男性向け" value="male"></v-radio>
          <v-radio label="女性向け" value="female"></v-radio>
          <v-radio label="オリジナル" value="original"></v-radio>
          <v-radio label="新人" value="rookie"></v-radio>
          <v-radio label="R18(日間)" value="daily_r18"></v-radio>
          <v-radio label="R18(週間)" value="weekly_r18"></v-radio>
          <v-radio label="男性向けR18" value="male_r18"></v-radio>
          <v-radio label="女性向けR18" value="female_r18"></v-radio>
          <v-radio label="R18G" value="r18g"></v-radio>
        </v-radio-group>
      </v-card-text>
      <v-divider></v-divider>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue" text @click="submitBtnClicked()">決定</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
  import spinner from '../spinner.vue'

  export default {
    components: {
      spinner
    },
    data () {
      return {
        rankingGenre: '',
        rankingGenreDialog: false,
      }
    },
    methods: {
      async submitBtnClicked() {
        if(this.rankingGenre === "") {
          alert('ランキングを選択してください。')
          return false
        }

        // ローディングをセット
        this.$store.commit('set_loading')
        await this.axios.get('http://127.0.0.1:8000/get_pixiv_ranking?genre=' + this.rankingGenre)
          .then(() => {
            // ローディングを解除
            this.$store.commit('set_loading');
            // モーダルを閉じる
            this.rankingGenreDialog = false;

          })
          .catch(err=> {
            alert('通信エラーが発生しました。');
            console.log("Error Occurred!",err);
          });
          // 再度スライドショーを描画
          this.$router.go('/')
      }
    }
  }
</script>