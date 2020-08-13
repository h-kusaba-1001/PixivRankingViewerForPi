import Vue from "vue";
import VueRouter from "vue-router";
// import Home from "../views/Home.vue";
// import Calendar from "../components/Calendar.vue";
import Slide from "../components/Slide.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Slide
  }
];

const router = new VueRouter({
  mode: 'history',
  routes
});

export default router;
