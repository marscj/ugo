<template>
  <detail :is-edit="false" />
</template>

<script>
import Detail from './Detail'

export default {
  name: 'CreateForm',
  components: { Detail },
  data() {
    return {
      description: '新建产品',
    }
  }
}
</script>

