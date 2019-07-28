<template>
  <detail :is-edit="true" @title="onTitle"/>
</template>

<script>
import Detail from './Detail'

export default {
  name: 'CreateForm',
  components: { Detail },
  data() {
    return {
      description: '编辑订单',
    }
  },
  methods: {
    onTitle() {
      this.$parent.getPageMeta()
    }
  },
}
</script>

