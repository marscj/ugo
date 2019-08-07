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
      description: '编辑公告',
    }
  },
  methods: {
    onTitle(data) {
      this.description = data.variant
      this.pageTitle = data.product;
      this.$parent.getPageMeta()
    }
  },
}
</script>

