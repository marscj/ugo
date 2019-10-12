<template>
  <a-spin :spinning="loading">
    <a-card>
      <div slot="title">
        <a-dropdown :disabled="isEdit">
          <a-menu slot="overlay" @click="handleMenuClick">
            <a-menu-item v-for="data in Category" :key="data.value">
              <icon-font :type="data.type" />
              {{data.label}}
            </a-menu-item>
          </a-menu>
          <a-button style="margin-left: 8px">
            {{Category[form.category - 1].label}}
            <a-icon type="down" />
          </a-button>
        </a-dropdown>
      </div>

      <!-- <div slot="extra">
        <a-button v-if="isEdit" type="primary" @click="update">Update</a-button>
        <a-button v-else type="primary" @click="create">Create</a-button>
      </div> -->

      <hotel v-if="form.category == 5" />

    </a-card>
  </a-spin>
</template>

<script>
import { Icon } from "ant-design-vue";
import { createBooking, updateBooking, getBooking } from "@/api/booking";
import moment from "moment";

import Hotel from "./hotel";

const IconFont = Icon.createFromIconfontCN({
  scriptUrl: "//at.alicdn.com/t/font_1402881_gsh78a0lnya.js"
});

const Category = [
  { value: 1, label: "Restaurant", type: "iconf-30" },
  { value: 2, label: "Tour", type: "iconticket" },
  { value: 3, label: "Transport", type: "iconche" },
  { value: 4, label: "Car", type: "iconche" },
  { value: 5, label: "Hotel", type: "iconhotel" },
  { value: 6, label: "Gift", type: "iconliwu1" }
];

export default {
  props: {
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  components: {
    IconFont, Hotel
  },
  data() {
    return {
      Category,
      loading: false,
      form: {
        category: 1,
      }
    }
  },
  methods: {
    handleMenuClick(e) {
      this.form.category = e.key;
    }
  },
};
</script>

<style >
.form-item {
  margin-bottom: 16px;
  color: red;
}
</style>