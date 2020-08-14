<template>
  <v-toolbar 
  dark
  max-height="60"
  min-height="60">
    <v-toolbar-title>Pixiv Ranking Viewer</v-toolbar-title>
    <v-spacer></v-spacer>
    <SelectRankingGenre></SelectRankingGenre>
  </v-toolbar>
</template>

<script>
	import SelectRankingGenre from "../components/modal/SelectRankingGenre";

	export default {
	name: "App",
	components: {
	  SelectRankingGenre
	},
	data: () => ({
			items: [],
		})
	};
</script>
