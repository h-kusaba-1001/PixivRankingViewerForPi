<script>
import FullCalendar from "@fullcalendar/vue";
import dayGridPlugin from "@fullcalendar/daygrid";
import allLocales from "@fullcalendar/core/locales-all";
import Const from "../../const/const";

export default {
  components: {
    FullCalendar // make the <FullCalendar> tag available
  },
  computed: {
    calanderConfig() {
      return {
        ...this.calanderConfigOptions
      };
    },
    calanderConfigOptions() {
      return {
        plugins: [dayGridPlugin],
        initialView: "dayGridMonth",
        locales: allLocales,
        locale: Const.LOCALE, // ja
        headerToolbar: {
          left: "prev,next today",
          center: "title",
          right: ""
        }
      };
    }
  },
  data() {
    return {};
  }
};
</script>

<template>
  <div>
    <FullCalendar :options="calanderConfig" />
  </div>
</template>


<style>
    * {
        padding: 0;
        margin: 0;
        box-sizing: border-box;
    }
    html, body {
        height: 100vh;
    }
     body {
        font-family: Arial, Helvetica Neue, Helvetica, sans-serif;
        font-size: 14px;
     }
</style>

<style scoped>
    #app {
        display: flex;
        overflow: hidden;
        height: 100%;
    }
    .calendar {
        flex: 1;
        padding: 2em;
    }
</style>