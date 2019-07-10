<template>
  <detail :is-edit="true" />
</template>

<script>
import Detail from './Detail'

export default {
  name: 'CreateForm',
  components: { Detail },
  data() {
    return {
      description: '编辑产品',
    }
  }
}
</script>

