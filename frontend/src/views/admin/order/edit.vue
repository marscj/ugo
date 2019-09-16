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
      description: '',
    }
  },
  methods: {
    onTitle(data) {
      this.$route.meta.title = data.orderID;
      // this.$parent.getPageMeta()
    }
  },
}
</script>

