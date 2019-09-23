<template>
  <detail :is-edit="false" />
</template>

<script>
import Detail from './Detail'

export default {
  name: 'CreateCoupon',
  components: { Detail },
  data() {
    return {
      description: '新建优惠券',
    }
  }
}
</script>

