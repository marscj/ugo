<template>
  <a-spin :spinning="loading">
    <a-card>
      <template slot="title" v-if="form">
        <icon-font :type="Category[form.category].type" />
        {{Category[form.category].label}}
      </template>
      <restaurant
        ref="form"
        v-if="form && form.category == 1"
        :isEdit="true"
        @onTitle="onTitle"
        @update="update"
      />
      <tour
        ref="form"
        v-if="form && form.category == 2"
        :isEdit="true"
        @onTitle="onTitle"
        @update="update"
      />
      <transport
        ref="form"
        v-if="form && form.category == 3"
        :isEdit="true"
        @onTitle="onTitle"
        @update="update"
      />
      <hotel
        ref="form"
        v-if="form && form.category == 4"
        :isEdit="true"
        @onTitle="onTitle"
        @update="update"
      />
    </a-card>
  </a-spin>
</template>

<script>
import { getBooking, updateBooking } from "@/api/booking";

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
  name: "BookingCreate",
  components: {
    IconFont,
    Hotel,
    Tour,
    Restaurant,
    Transport
  },
  mounted() {
    this.fetch(this.$route.params.id);
  },
  data() {
    return {
      Category,
      form: null,
      loading: false
    };
  },
  methods: {
    onTitle(data) {
      this.$route.meta.title = data.bookingID;
      this.$parent.getPageMeta();
    },
    fetch(id) {
      this.loading = true;
      getBooking(id)
        .then(res => {
          const { result } = res;
          this.form = result;
          this.onTitle(this.form);

          this.$nextTick(() => {
            this.$refs.form.onFetch(this.form);
          });
        })
        .finally(() => {
          this.loading = false;
        });
    },
    update(data) {
      this.loading = true;
      updateBooking(data.id, data)
        .then(res => {
          const { result } = res;
          this.$nextTick(() => {
            this.$refs.form.onUpdate(this.form);
          });
        })
        .finally(() => {
          this.loading = false;
        });
    }
  }
};
</script>