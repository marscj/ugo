<template>
  <detail :is-edit="false" />
</template>

<script>
import Detail from './Detail'

export default {
  name: 'CreateForm',
  components: { Detail }
}
</script>

