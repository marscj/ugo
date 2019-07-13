<template>
<div class="div-height">
  <a-menu
    v-model="current"
    mode="horizontal"
  >
    <a-menu-item key="mail">
      首页
    </a-menu-item>
    <a-menu-item key="app">
      门票
    </a-menu-item>
    <a-sub-menu>
      <span slot="title" class="submenu-title-wrapper">美食</span>
      <a-menu-item key="setting:1">Option 1</a-menu-item>
      <a-menu-item key="setting:2">Option 2</a-menu-item>
      <a-menu-item key="setting:3">Option 3</a-menu-item>
      <a-menu-item key="setting:4">Option 4</a-menu-item>
    </a-sub-menu>
    <a-menu-item key="alipay">
      玩乐
    </a-menu-item>
  </a-menu>

  
</div>
</template>
<script>
export default {
  data () {
    return {
      current: ['mail'],
    }
  },
}
</script>

<style> 
  .div-height{
    text-align: center;
    padding: 30px 0;
  } 
</style> 
