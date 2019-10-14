<template>
  <a-spin :spinning="loading">
    <a-card>
      <template slot="title">
        <icon-font :type="Category[$route.query['type']].type" />
        {{Category[$route.query['type']].label}}
      </template>
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

import { Icon } from "ant-design-vue";
const IconFont = Icon.createFromIconfontCN({
  scriptUrl: "//at.alicdn.com/t/font_1402881_gsh78a0lnya.js"
});

const Category = [
  { value: 1, label: "Restaurant", type: "iconf-30" },
  { value: 2, label: "Tour", type: "iconticket" },
  { value: 3, label: "Transport", type: "iconche" },
  { value: 4, label: "Hotel", type: "iconhotel" }
];

export default {
  props: {
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  components: {
    IconFont,
    Hotel,
    Tour,
    Restaurant,
    Transport
  },
  data() {
    return {
      Category,
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