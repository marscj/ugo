<template>
  <detail :is-edit="true" @title="onTitle"/>
</template>

<script>
import Detail from './Detail'

export default {
  name: 'EditCoupon',
  components: { Detail },
  data() {
    return {
      description: '编辑优惠券',
    }
  },
  methods: {
    onTitle() {
      this.$parent.getPageMeta()
    }
  },
}
</script>

