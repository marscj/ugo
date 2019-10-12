<template>
  <a-card>
    <div slot="title">
      <a-dropdown>
        <a-menu slot="overlay" @click="handleMenuClick">
          <a-menu-item v-for="data in Category" :key="data.value">
            <icon-font :type="data.type" />
            {{data.label}}
          </a-menu-item>
        </a-menu>
        <a-button style="margin-left: 8px">
          <icon-font :type="Category[category - 1].type" />
          {{Category[category - 1].label}}
          <a-icon type="down" />
        </a-button>
      </a-dropdown>
    </div>

    <hotel v-if="category == 5" :isEdit="isEdit" />
    <tour v-if="category == 2" :isEdit="isEdit" />
    <restaurant v-if="category == 1" :isEdit="isEdit" />
  </a-card>
</template>

<script>
import { Icon } from "ant-design-vue";

const IconFont = Icon.createFromIconfontCN({
  scriptUrl: "//at.alicdn.com/t/font_1402881_gsh78a0lnya.js"
});

import Hotel from "./hotel";
import Tour from "./tour";
import Restaurant from "./restaurant";

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
    IconFont,
    Hotel,
    Tour,
    Restaurant
  },
  data() {
    return {
      Category,
      loading: false,
      category: 1
    };
  },
  methods: {
    handleMenuClick(e) {
      this.category = e.key;
    },

    create(data) {
      console.log("create");
    },

    update(data) {
      console.log("update");
    }
  }
};
</script>

<style >
.form-item {
  margin-bottom: 16px;
  color: red;
}
</style>