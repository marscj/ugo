<template>
  <div>
    <h1>
      {{title}}
    </h1>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: 'abc'
    }
  },
}
</script>
