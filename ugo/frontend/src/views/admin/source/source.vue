<template>
  <a-card :bordered="false">
    <source-list/>
  </a-card>
</template>

<script>
import SourceList from './SourceList'
export default {
  name:'Source',
  components: {
    SourceList
  },
  data() {
    return {
        
    }
  }
}
</script>
