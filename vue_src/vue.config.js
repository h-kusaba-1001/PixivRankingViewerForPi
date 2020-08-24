module.exports = {
  outputDir: "../serverside_src",
  publicPath: "/",
  indexPath: "api/templates/api/index.html",
  assetsDir: "static",
  // devServer: {
  //   proxy: {
  //     "/api/": {
  //       target: "http://127.0.0.1:8000",
  //     },
  //   },
  // },
  // devServer: {
  //   proxy: "http://127.0.0.1:8000",
  // },
  transpileDependencies: ["vuetify"],
};