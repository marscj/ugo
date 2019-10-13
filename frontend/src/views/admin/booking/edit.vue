<template>
  <a-card>
    
    <restaurant v-if="$route.query['category'] == 1" :isEdit="true" @onTitle="onTitle"/>
    <tour v-if="$route.query['category'] == 2" :isEdit="true" @onTitle="onTitle"/>
    <transport v-if="$route.query['category'] == 3" :isEdit="true" @onTitle="onTitle"/>
    <hotel v-if="$route.query['category'] == 5" :isEdit="true" @onTitle="onTitle"/>
  </a-card>
</template>

<script>
import Hotel from "./hotel";
import Tour from "./tour";
import Restaurant from "./restaurant";
import Transport from "./transport";

export default {
  name: "BookingCreate",
  components: {
    Hotel, Tour , Restaurant, Transport
  },
  methods: {
    onTitle(data) {
      this.$route.meta.title = data.bookingID
      this.$parent.getPageMeta()
    }
  },
};
</script>