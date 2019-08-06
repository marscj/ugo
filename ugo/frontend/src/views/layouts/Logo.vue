<template>
  <div >
    <router-link :to="{name:'Home'}">
      <!-- <LogoSvg alt="logo" class="logo"/> -->
      <img src="~@/assets/logo.svg" class="logo" alt="logo">
    </router-link>
  </div>
</template>

<script>
import LogoSvg from "@/assets/logo.svg?inline";

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

<style>
/* .logo {
  height: 75px;
  vertical-align: top;
  margin-right: 16px;
  padding-top: 10px;
  border-style: none;
} */
.logo {
  position: relative;
  height: 58px;
  padding-left: 24px;
  overflow: hidden;
  line-height: 58px;
  transition: all 0.3s;
}
</style>

