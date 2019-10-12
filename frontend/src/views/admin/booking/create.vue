<template>
  <div>
    <detail :isEdit="false" />
  </div>
</template>

<script>
import { createBooking } from "@/api/booking";
import Detail from "./detail";

export default {
  name: "BookingCreate",
  components: {
    Detail,
  },
};
</script>