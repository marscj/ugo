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
      description: '新建子产品',
    }
  }
}
</script>

