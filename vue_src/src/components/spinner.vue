<template>
  <div class="text-center" 
	v-show="loading"
	:elevation="15"
	style="height: auto; width:auto ;">
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
		components: {
		},
		computed: {
			loading() {
				return this.$store.state.loading
			}
		}
	};
</script>