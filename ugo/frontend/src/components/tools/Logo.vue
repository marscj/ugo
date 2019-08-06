<template>
  <div class="logo">
    <router-link :to="{name:'dashboard'}">
      <LogoSvg alt="logo" />
      <!-- <img src="~@/assets/logo.png" class="logo" alt="logo"/> -->
      <h1 v-if="showTitle">{{ title }}</h1>
    </router-link>
  </div>
</template>

<script>
import LogoSvg from "@/assets/logo.png";

export default {
  name: "Logo",
  components: {
    LogoSvg
  },
  props: {
    title: {
      type: String,
      default: "",
      required: false
    },
    showTitle: {
      type: Boolean,
      default: true,
      required: false
    }
  }
};
</script>
<style >
.logo {
  height: 144px;
  vertical-align: top;
  margin-right: 16px;
  border-style: none;
}
</style>