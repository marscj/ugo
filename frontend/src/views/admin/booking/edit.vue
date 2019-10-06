<template>
  <detail :isEdit="true" :order="order" />
</template>

<script>
import Detail from "./detail";

export default {
  name: "BookingCreate",
  props: {
    order: {
      type: Object,
      default: undefined
    }
  },
  components: {
    Detail
  }
};
</script>