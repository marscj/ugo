<template>
  <a-spin :spinning="loading">
    <a-card>
      <restaurant v-if="$route.query['type'] == 1" :isEdit="false" @create="create" />
      <tour v-if="$route.query['type'] == 2" :isEdit="false" @create="create" />
      <transport v-if="$route.query['type'] == 3" :isEdit="false" @create="create" />
      <hotel v-if="$route.query['type'] == 4" :isEdit="false" @create="create" />
    </a-card>
  </a-spin>
</template>

<script>
import { createBooking } from "@/api/booking";

import Hotel from "./hotel";
import Tour from "./tour";
import Restaurant from "./restaurant";
import Transport from "./transport";

export default {
  props: {
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  components: {
    Hotel,
    Tour,
    Restaurant,
    Transport
  },
  data() {
    return {
      loading: false
    };
  },
  methods: {
    create(data) {
      this.loading = true;
      createBooking(data)
        .then(res => {
          const { id } = res.result;
          this.$router.replace({
            name: "BookingEdit",
            params: { id }
          });
        })
        .finally(() => {
          this.loading = false;
        });
    }
  }
};
</script>