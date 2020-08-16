import Vue from "vue";
import VueRouter from "vue-router";
// import Home from "../views/Home.vue";
// import Calendar from "../components/Calendar.vue";
import Main from "../components/Main.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Main",
    component: Main
  }
];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router;
